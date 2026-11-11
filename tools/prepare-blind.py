import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from review_packets import make_blind,make_cross,final_gate
a=json.load(sys.stdin)
print(json.dumps(make_blind(a['source']),ensure_ascii=False))
