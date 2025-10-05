import os
import yaml
from pathlib import Path

repo_root = Path(__file__).parent.parent
mappings_dir = repo_root / "Mappings"

combined_data = {}

for yaml_file in mappings_dir.rglob("TMDB Order.yaml"):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
        if data:
            combined_data.update(data)

sorted_data = dict(sorted(combined_data.items(), key=lambda x: int(x[0])))

def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')

yaml.SafeDumper.add_representer(type(None), represent_none)

output_file = repo_root / "All TMDB.yaml"
with open(output_file, 'w', newline='\n') as f:
    yaml.dump(sorted_data, f, default_flow_style=False, sort_keys=False, indent=2, allow_unicode=True, Dumper=yaml.SafeDumper)
