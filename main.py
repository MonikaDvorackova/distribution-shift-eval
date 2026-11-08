import csv,sys
def metrics(rows):
    if not rows:return {'n':0}
    acc=sum((float(r['p'])>=.5)==bool(int(r['y'])) for r in rows)/len(rows)
    brier=sum((float(r['p'])-int(r['y']))**2 for r in rows)/len(rows)
    return {'n':len(rows),'accuracy':acc,'brier':brier}
def run(path):
    with open(path,encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    result={}
    for split in sorted({r['split'] for r in rows}):
        part=[r for r in rows if r['split']==split];result[split]={'overall':metrics(part),'groups':{g:metrics([r for r in part if r['group']==g]) for g in sorted({r['group'] for r in part})}}
    return result
if __name__=='__main__':
    import json;print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else 'data/predictions.csv'),indent=2))
