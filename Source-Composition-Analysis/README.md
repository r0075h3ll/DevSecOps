## Source Composition Analysis for Java

![pipeline](/design.png)

Visibility is often overlooked, but is rather an important part of DevSecOps. With the shift-left philosophy being a priority for organizations - in order to induce
faster, and secure product releases, Source Composition Analysis (SCA) provides a heads-up on all the integrated third-party and OSS software components. It
allows a security engineering team to assess risks effectively. 


As shift-left suggests the integration of security into developer workflows, so, let's see how we can implement SCA in Gitlab CI pipelines.

Steps:
1. Include `'org.cyclonedx.bom'` plugin in the build script (`build.gradle`)
2. Specify plugin configurations in `sca.gradle` 
3. Include `SBOM.gitlab-ci.yml` in the CI config of a repository

Futhermore, the jobs can be configured to run on
- events
- schedules


### References

- https://github.com/CycloneDX/cyclonedx-gradle-plugin