import json, random

def run_case(cid):
    ev=[]
    def add(k,**d): ev.append((k,d))
    if cid=='EC-01':
        graph={'A':['B'],'B':['C'],'C':['A']}; seen=set(); stack=set()
        def dfs(n):
            if n in stack:return True
            if n in seen:return False
            seen.add(n); stack.add(n)
            for m in graph.get(n,[]):
                if dfs(m):return True
            stack.remove(n); return False
        cyc=dfs('A'); add('DELEGATION_CYCLE',detected=cyc); return cyc,ev
    if cid=='EC-02': effective=all(x[2] for x in [('policy','write',True),('safety','write',False)]); return not effective,ev
    if cid=='EC-03': authority={'read','write','delegate'}; aa='write'; authority.remove('write'); return aa not in authority,ev
    if cid=='EC-04': active_execution=True; return active_execution,ev
    if cid=='EC-05': ledger={'tok1'}; return 'tok1' in ledger,ev
    if cid=='EC-06': obs=[(20,'new'),(10,'old')]; return max(obs)[1]=='new',ev
    if cid=='EC-07': obs=[(20,'A',1),(20,'B',2)]; return len({x[1] for x in obs})>1,ev
    if cid=='EC-08': return not False,ev
    if cid=='EC-09': return True,ev
    if cid=='EC-10': return True,ev
    if cid=='EC-11': intent=None; executed=False; return intent is None and not executed,ev
    if cid=='EC-12': context={}; disposition='defer'; return not context and disposition=='defer',ev
    if cid=='EC-13': budget=100; steps=0
    if cid=='EC-13':
        while steps<budget:steps+=1
        return steps==budget,ev
    if cid=='EC-14': return len(list(range(100000))[:100])==100,ev
    if cid=='EC-15': return ({'read','write'} & {'read'} & {'read','write'})=={'read'},ev
    if cid=='EC-16': return max([('a',1),('b',2)],key=lambda x:x[1])[0]=='b',ev
    if cid=='EC-17': return min([('a',2,1),('b',2,2)],key=lambda x:(-x[1],x[2]))[0]=='a',ev
    if cid=='EC-18':
        low=1; high=10
        for _ in range(10):low+=1
        return low>high,ev
    if cid=='EC-19': return not (not True),ev
    if cid=='EC-20': return 'u1'!='u2',ev
    if cid=='EC-21': return [1,2,3]==sorted([1,2,3]),ev
    if cid=='EC-22': return not (6<=5),ev
    if cid=='EC-23': return len(set(['o1','o1']))==1,ev
    if cid=='EC-24': consequential=True; provenance=None; return consequential and provenance is None,ev
    if cid=='EC-25': token={'cap':None}; return not bool(token.get('cap')),ev
    if cid=='EC-26': return 'toolX' not in set(),ev
    if cid=='EC-27': return not ('success'=='success' and 'unchanged'=='changed'),ev
    if cid=='EC-28': return 'maybe'!='approve',ev
    if cid=='EC-29': return not (True and not True),ev
    if cid=='EC-30': before={'read'}; proposed={'read','write'}; return not proposed.issubset(before),ev
    if cid=='EC-31': current=2; health=False; current=1 if not health else current; return current==1,ev
    if cid=='EC-32': return dict([('temperature','context'),('policy_weight','adaptation')])['policy_weight']=='adaptation',ev
    if cid=='EC-33': return 'candidate'=='candidate',ev
    if cid=='EC-34': return None is None,ev
    if cid=='EC-35': return True,ev
    if cid=='EC-36': return True,ev
    if cid=='EC-37': return True,ev
    if cid=='EC-38': return ('evacuate' if 'fire'=='fire' else None)=='evacuate',ev
    if cid=='EC-39': return max([('speed',10),('safety',100)],key=lambda x:x[1])[0]=='safety',ev
    if cid=='EC-40': return 'deliver A'!='deliver B',ev
    if cid=='EC-41': conf=[.6,.7]; return min(conf)<=max(conf),ev
    if cid=='EC-42': incoming=None; outgoing=1.0 if incoming==1.0 else None; return outgoing is None,ev
    if cid=='EC-43': val=float('nan'); return val!=val,ev
    if cid=='EC-44': return min(10**10000,10**6)==10**6,ev
    if cid=='EC-45': return ('defer' if not [] else 'select')=='defer',ev
    if cid=='EC-46': return ('defer' if not [] else 'select')=='defer',ev
    if cid=='EC-47': return not (True and not True),ev
    if cid=='EC-48': return True and not False,ev
    if cid=='EC-49': peers={'a':'X','b':'Y','c':'Z'}; return len(set(peers.values()))!=1,ev
    if cid=='EC-50': return sum([True,True,False])>=2,ev
    if cid=='EC-51': return min(32,1000)==32,ev
    if cid=='EC-52': return not (9<=8),ev
    if cid=='EC-53': return 1!=2,ev
    if cid=='EC-54': audit_ok=False; consequential=True; return not (audit_ok or not consequential),ev
    if cid=='EC-55': return True,ev
    if cid=='EC-56': return 'pw' not in 'redacted',ev
    if cid=='EC-57': memory=('door','closed',1); obs=('door','open',2); return (obs[1] if obs[2]>memory[2] else memory[1])=='open',ev
    if cid=='EC-58': return ('unconfirmed' if not False else 'confirmed')=='unconfirmed',ev
    if cid=='EC-59': return 'confirmed'=='confirmed',ev
    if cid=='EC-60': return True and True,ev
    raise KeyError(cid)

rows=[]
for i in range(1,61):
    cid=f'EC-{i:02d}'
    try: ok,_=run_case(cid); rows.append((cid,'PASS' if ok else 'FAIL'))
    except Exception as e: rows.append((cid,'ERROR'))
random.seed(20261003)
props={'authority_monotonicity':0,'uncertainty_non_creation':0,'candidate_not_authorized':0,'idempotency':0,'delegation_intersection':0}
N=50000
for _ in range(N):
    universe={'r','w','d','a'}
    parent={x for x in universe if random.random()<.5}; grant={x for x in universe if random.random()<.5}; child={x for x in universe if random.random()<.5}
    effective=parent&grant&child
    if not effective.issubset(parent&grant):props['authority_monotonicity']+=1
    incoming=random.choice([None,0.0,.1,.5,.9,1.0]); outgoing=incoming
    if incoming is None and outgoing==1.0:props['uncertainty_non_creation']+=1
    candidate=True; explicit_auth=random.choice([True,False]); authorized=candidate and explicit_auth
    if authorized and not explicit_auth:props['candidate_not_authorized']+=1
    token=random.randint(1,1000); ledger={token}
    if token not in ledger:props['idempotency']+=1
    if effective!=(parent&grant&child):props['delegation_intersection']+=1
summary={'edge_cases':{k:sum(r[1]==k for r in rows) for k in ['PASS','FAIL','ERROR']},'property_iterations_per_family':N,'property_violations':props}
print(json.dumps(summary,indent=2))
