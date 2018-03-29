# RESTful API service to enable ease of portability leveraging boto/libcloud

Harshad Patkar, Sushant Athaley, Michael Robinson

## Keywords

hid-sp18-517, hid-sp18-402, hid-sp18-518, boto, libcloud

## Abstract

Our research will measure how the portability of an application is impacted by decisions made early in the software lifecycle when native cloud provider APIs are used. We will demonstrate how efforts to leverage scalable, reproducable solutions like boto and libcloud are advantageous. We will derive reproducable code using Swagger and Python to show how libraries like boto and libcloud can be used to migrate an application from one cloud provider to another with a measurable reduction in human error and with less time to execute. Additionally, we will leverage Swagger to develop RESTful APIs to further improve the gains. We will capture the results of the research, share the derived code and conclude how the research can be applied to existing and new development efforts intending to leverage cloud providers.

## Introduction

The solution we will derive will further abstract attempts for portability to RESTful APIs. Developers are already confronted with many a lack of transparency on which cloud provider is optimal for the long-term sustainability of their application. Additionally, attempts to abstract cloud providers has helped yet still potentially locks you into solutions provided by Apache or communities like boto. Leveraging REST, we intend to introduce a standardized implementation that leverages cloud portability libraries to manage the diversity of cloud applications. A high-level abstract of our final concept is below.

Table 1: Project Architecture

![Project Architecture](https://github.com/cloudmesh-community/hid-sp18-518/blob/master/project/images/proj_arch.png?raw=true)

## Scope of work
- Value Hypothesis
- Cycle time metrics on porting a solution without boto/libcloud
- Lead time metrics on use of RESTful APIs compared to command line usage
- RESTful API
  - Swagger development to design/build API services for UI
  - Python development to leverage boto/libcloud
  - Evidence of success porting a solution from/to AWS, Azure, Google Cloud, OpenStack
- Comparison of porting solution manually to libcloud/boto by command line
- Comparison of porting solution with libcloud/boto by commandline to RESTful API solution
- Conclusion

## Special Consideration to Project Format
- Swagger API documentation
- Comparison of command line tools to Python libraries libcloud and boto

## References
- D. Petcu and A. Vasilakos, *Portability in Clouds: Approaches and Research Opportunities*, Scalable Computing: Practice and Experience, Vol. 15 No. 3, 2014, https://scpe.org/index.php/scpe/
- Cloud Security Council, *Interoperability and Portability for Cloud
Computing*, 2017, http://www.cloud-council.org/deliverables/CSCC-Interoperability-and-Portability-for-Cloud-Computing-A-Guide.pdf
- M. Kostoska, M. Gusev and S. Ristov, *A New Cloud Services Portability Platform*, Procedia Engineering, Vol. 69, 2014, https://doi.org/10.1016/j.proeng.2014.03.118
- L. Badger, D. Bernstein, R. Bohn, F. de Vaulx, M. Hogan, M. Iorga, J. Mao, J. Messina, K. Mills, E. Simmon, A. Sokol, J. Tong, F. Whiteside and D. Leaf, *High-Priority Requirements to Further USG Agency Cloud Computing Adoption*, Special Publication 500-293, https://dx.doi.org/10.6028/NIST.SP.500-293
