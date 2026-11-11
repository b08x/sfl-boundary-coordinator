"""Offline schema, role-boundary, DAG and reference validation."""
from pathlib import Path
from graphlib import TopologicalSorter
import json,re,yaml
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
def schema(name):return json.loads((ROOT/f'spec/upstream/{name}.schema.json').read_text())
def check(kind,data):Draft202012Validator(schema(kind)).validate(data)
def main():
 root=yaml.safe_load((ROOT/'agent.yaml').read_text());agents={root['name']:root}
 expected=set(root['agents']);actual={p.name for p in (ROOT/'agents').iterdir() if p.is_dir()}
 assert expected==actual,'sub-agent roster differs from disk'
 for d in [ROOT,*sorted((ROOT/'agents').iterdir())]:
  m=yaml.safe_load((d/'agent.yaml').read_text());check('agent-yaml',m);agents[m['name']]=m
  assert d.name==m['name'],'directory/name mismatch'
  for f in ['SOUL.md','RULES.md','PROMPT.md']:assert (d/f).read_text().strip(),f
  for s in m.get('skills',[]):assert (d/'skills'/s/'SKILL.md').is_file(),s
  for t in m.get('tools',[]):assert (d/'tools'/f'{t}.yaml').is_file(),t
 for p in ROOT.glob('**/skills/*/SKILL.md'):
  if 'migration' in p.parts:continue
  fm=yaml.safe_load(p.read_text().split('---',2)[1]);check('skill',fm);assert fm['name']==p.parent.name
 for p in (ROOT/'tools').glob('*.yaml'):
  t=yaml.safe_load(p.read_text());check('tool',t);assert t['name']==p.stem
  assert (p.parent/t['implementation']['path']).is_file()
 for p in (ROOT/'workflows').glob('*.yaml'):
  w=yaml.safe_load(p.read_text());check('workflow',w)
  steps={s['id']:s for s in w['steps']};assert len(steps)==len(w['steps'])
  deps={k:set(v.get('depends_on',[])) for k,v in steps.items()}
  assert all(v<=steps.keys() for v in deps.values());list(TopologicalSorter(deps).static_order())
  def ancestors(k):return set().union(*(ancestors(x)|{x} for x in deps[k])) if deps[k] else set()
  inputs={x['name'] for x in w.get('inputs',[])}
  for k,s in steps.items():
   if 'agent' in s:assert s['agent'] in expected
   if 'tool' in s:assert s['tool'] in root['tools']
   for src,key in re.findall(r'\$\{\{ steps\.([\w-]+)\.outputs\.([\w-]+) \}\}',json.dumps(s)):
    assert src in ancestors(k) and key in steps[src].get('outputs',[]),(k,src,key)
   for key in re.findall(r'\$\{\{ inputs\.([\w-]+) \}\}',json.dumps(s)):assert key in inputs
 sod=root['compliance']['segregation_of_duties'];roleids={x['id'] for x in sod['roles']}
 assert set(sod['assignments'])==set(agents)
 for n,rs in sod['assignments'].items():
  assert set(rs)<=roleids
  for a,b in sod['conflicts']:assert not {a,b}<=set(rs),(n,a,b)
 for h in sod['handoffs']:assert set(h['required_roles'])<=set().union(*map(set,sod['assignments'].values()))
 for n,m in agents.items():
  if n.endswith('-judge'):assert m.get('tools')==[] and not m.get('agents') and not m.get('mcp_servers')
 print(f'PASS: {len(agents)} manifests, tools, skills, SOD, workflow DAG and data references')
if __name__=='__main__':main()
