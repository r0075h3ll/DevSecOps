> 🚧 Work In Progress
> To Do
> - Option flag to choose b/w different models
> - Clean JSON Output

### Introduction

The basic idea behind this implementation is to use regularly updated CT logs sources to hunt for potential typo-squatting and look-alike domains. Under the hood, we'll be using the power of semantics for improved detection.

Moving forward, a custom scraping framework can come handy, in case a domain scores high in terms of semantic similarity, to classify it as impersonation if a classifier trained on brand's data predicts so.

### Usage

```commandline
uv run python3 -m Typo-Squat-Detector -d fortesting -o output.json
```

[Output](/Typo-Squat-Detector/output.json) provides with semantic similarity b/w your input and newly found domains via `crt.sh`.

### Data Cleaning

crt.sh hosts Certificate Transparency Logs that helps in domain discovery, going further, the collected set of domains becomes the search space.

With the intent of making the data more relevant(clean) in our case, we'll only keep root domain, and sometimes the TLD i.e. the parts of domain name that preserve the semantics, and not something as 'www'.
