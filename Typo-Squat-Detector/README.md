> 🚧 Work In Progress

### Introduction

The basic idea behind this implementation is to use regularly updated CT logs sources to hunt for potential typo-squatting domains. Under the hood, we'll be using the power of semantics for improved detection.

### Usage

```commandline
uv run python3 -m Typo-Squat-Detector -d fortesting -o output.json
```

[Output](/Typo-Squat-Detector/output.json) provides with semantic similarity b/w your input and newly found domains via `crt.sh`.