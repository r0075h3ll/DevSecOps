import argparse
import json

from sentence_transformers import SentenceTransformer, util

from ct_logger import get_ct_logs, log_domains
from . import logger

parser = argparse.ArgumentParser()
parser.add_argument('-d', help='domain', dest='domain')
parser.add_argument('-s', help='similarity threshold', dest='sim_thres')
parser.add_argument('-o', help='write output to a file (default: stdout)', default='stdout', dest='output')

args = parser.parse_args()

model = SentenceTransformer('all-MiniLM-L6-v2')
domain = args.domain
sim_details = {'input_domain': f'{domain}', 'results': []}

if args.domain is None:
    exit(parser.print_usage())


def main():
    domains, _ = log_domains(get_ct_logs())

    target_emb = model.encode(domain)
    # cert_log_file = ''

    for new_domain in domains:
        emb_d = model.encode(new_domain)
        cos_similarity = util.cos_sim(target_emb, emb_d)

        sim_details['results'].append({
            f'{new_domain}': f'{cos_similarity}'
        })

    json_output = json.dumps(sim_details, indent=4)
    if args.output == 'stdout':
        print(json_output)
    else:
        with open(args.output, 'w') as file:
            file.write(json_output)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.debug(e)
