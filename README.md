## Reachability Analysis

Risk Management and Prioritization is a crucial aspect for application security posture management. In this era of SAST and SCA, where there are enough tools that generate findings on using known vulnerable components and dangerous functions - there are not many open-source solutions that give you any idea on the reachability i.e. whether or not there's a data flow path to the flagged vulnerable component.


Our objective w/ this would be to generate a working POC for testing the reachability analysis pipeline. 
- [ ] Take a sample REST API Project
- [ ] Add vulnerable code to routes
- [ ] Visualize access path for the vulnerable component(s)

![](https://i.ibb.co/XVSVFfq/map.png)


References
- https://www.endorlabs.com/learn/5-types-of-reachability-analysis-and-which-is-right-for-you