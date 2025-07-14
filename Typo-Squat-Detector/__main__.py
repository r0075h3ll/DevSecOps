import arparse
from . import logger
from sentence_transformers import SentenceTransformer, util

parser = arparse.ArgumentParser()
parser.add_argument('-d', help='domain', dest='domain')
parser.add_argument('-s', help='similarity threshold', dest='sim_thres')

args = parser.parse_args()

model = SentenceTransformer('all-MiniLM-L6-v2')
domain = args.domain

def main():
    target_emb = model.encode(domain)
    cert_log_file = ''

    for new_domain in cert_log_file:
        emb_d = model.encode(new_domain)
        cos_similarity = util.cos_sim(target_emb, emb_d)

        logger.info(f'New Domain Registered: {new_domain}\nSimilarity: {cos_similarity}')

if __name__ == "__main__":
    main()
