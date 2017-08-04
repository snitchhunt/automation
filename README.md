# Snitch Hunt Automation
https://snitchhunt.org/

Your metadata can tell so much about you that those looking at it may not even need the content.

<br/>
Snitch Hunt is a game that, using mock data and identities, will show participants how much can be learnt about someone just from the phone and internet records that 22 government agencies can access without a warrant.

---
This is a very concise picture of the technical components and the use cases.

![](docs/snitch-hunt-tech-components.jpg)

---

Pre-requisites:

* [Docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose/install/)

### To deploy AWS ES

Run

``` sh
export AWS_ACCESS_KEY_ID=<YOUR AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<YOUR AWS_SECRET_ACCESS_KEY>

$ auto/setup-elasticsearch

```
