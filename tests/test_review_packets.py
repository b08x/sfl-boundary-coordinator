import copy,json,subprocess,sys,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'scripts'))
import review_packets as p
from review_mcp import Server
class Packets(unittest.TestCase):
 def setUp(self):
  self.source=dict(task_id='fixture',document_revision='1',repository_revision='abc',draft='Parser returns JSON.',register=dict(field='parser',tenor='peer',mode='written',genre='fixture',dial='Compressed',template='fixture',task_type='audit',output_contract={}))
  self.b=p.make_blind(self.source);self.identity={k:self.b[k] for k in p.IDENTITY}
  self.js=[dict(self.identity,phase='blind',judge=x,evidence_sha256=None,status='COMPLETE',verdict='PROVISIONAL',findings=[],summary={},blockers=[]) for x in sorted(p.JUDGES)]
  self.e=dict(self.identity,phase='evidence',status='COMPLETE',project='fixture',tier='Verify',graph=dict(generation='fixture-1',freshness='current',repository_revision='abc'),scope=['parser.py'],queries=[dict(tool='check_index_coverage',arguments={},pages_complete=True,pagination={})],coverage=dict(checked=True,paths=['parser.py'],state='clean',fallback=[],unresolved_ranges=[]),evidence=[dict(id='e1',kind='source',location='parser.py:1',excerpt='return json',claim_ids=['c1'])],claims=[dict(claim_id='c1',classification='supported',treatment='asserted',evidence_refs=['e1'],claim_type='positive')],assumptions=[],blockers=[])
 def cross(self):return p.make_cross(self.b,self.js,self.e)
 def final(self,c):
  js=[dict(j,phase='cross_examination',verdict='PASS',evidence_sha256=c['evidence_sha256']) for j in self.js]
  g=dict(self.identity,evidence_sha256=c['evidence_sha256'],gates={x:dict(status='PASS',reason='Synthetic fixture only') for x in ['process_coverage','modality','cohesion','connectives','negative_capability']})
  return p.final_gate(c,js,g)
 def test_complete_fixture(self):self.assertTrue(self.final(self.cross())['accepted'])
 def test_blind_strips_peer_evidence(self):
  b=p.make_blind(dict(self.source,evidence_packet=self.e,peer_findings=['secret']));self.assertNotIn('evidence_packet',b);self.assertNotIn('peer_findings',b)
 def test_changed_draft(self):
  self.b['draft']+=' Changed.'
  with self.assertRaises(p.ContractError):self.cross()
 def test_duplicate_judge(self):
  self.js[1]=copy.deepcopy(self.js[0])
  with self.assertRaises(p.ContractError):self.cross()
 def test_stale_evidence(self):
  self.e['document_revision']='0'
  with self.assertRaises(p.ContractError):self.cross()
 def test_blind_cannot_approve(self):
  self.js[0]['verdict']='PASS'
  with self.assertRaises(p.ContractError):self.cross()
 def test_unknown_claim_reference(self):
  self.e['claims'][0]['evidence_refs']=['missing']
  with self.assertRaises(p.ContractError):self.cross()
 def test_unsupported_assertion(self):
  self.e['claims'][0]['classification']='unsupported';self.assertFalse(self.final(self.cross())['accepted'])
 def test_unmeasured_scout(self):
  self.e['tier']='Scout';self.assertFalse(self.final(self.cross())['accepted'])
 def test_missing_coverage(self):
  self.e['queries'][0]['tool']='search_graph'
  with self.assertRaises(p.ContractError):self.cross()
 def test_tool_wrapper(self):
  r=subprocess.run([sys.executable,str(R/'tools/prepare-blind.py')],input=json.dumps({'source':self.source}),text=True,capture_output=True,check=True,cwd='/tmp');self.assertEqual(json.loads(r.stdout),self.b)
 def test_mcp_lifecycle(self):
  s=Server();self.assertIn('error',s.handle(dict(jsonrpc='2.0',id=1,method='tools/list')))
  s.handle(dict(jsonrpc='2.0',id=2,method='initialize',params={'protocolVersion':'2025-03-26'}));s.handle(dict(jsonrpc='2.0',method='notifications/initialized'))
  r=s.handle(dict(jsonrpc='2.0',id=3,method='tools/call',params={'name':'prepare_blind','arguments':{'source':self.source}}));self.assertFalse(r['result']['isError'])
if __name__=='__main__':unittest.main()
