### Part 3: Certificates and SSL with OpenSSL

OpenSSL can help us with handling digital certificates.
- Create a CA, sign and issue certificates using [OpenSSL](https://pki-tutorial.readthedocs.io/en/latest/) certificate tutorial
- The tutorial consists of three labs. Complete the Simple lab first. The subsequent Advanced and Expert labs are stretch goals.
  1. [Simple PKI](https://pki-tutorial.readthedocs.io/en/latest/simple/index.html)

We can use OpenSSL to monitor secure web server activity using HTTP GET request

- Create a script that automatically checks a website is properly handling SSL requests
  - Check for expired web certificates
- Create a script that automatically checks if a SSL certificate for a website is about to expire, and notifies admin

### Part 4: Reporting

## Stretch Goals (Optional Objectives) 

### Stretch Goal 1: OpenSSL Certificate Tutorials

  2. [Advanced PKI](https://pki-tutorial.readthedocs.io/en/latest/advanced/index.html)
  3. [Expert PKI](https://pki-tutorial.readthedocs.io/en/latest/expert/index.html)

### Stretch Goal 1: Windows Server proprietary CA implementation

- Deploy Windows CA service on your Windows Server
- Generate a signed certificate
- Assign certificate to a domained computer

### Stretch Goal 2: Where's the HTTPS?

- Add HTTPS to a website that doesn't have it yet
- Install HTTPSONLY to your web browser and navigate to a non-HTTP website
- Learn how to use encryption keys on AWS Cloud
  1. 50 mins - [Introduction to AWS Key Management Service](https://amazon.qwiklabs.com/focuses/10388?catalog_rank=%7B%22rank%22%3A3%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=5201321)
    1. Topics:
      1. Create an Encryption Key
      2. Create an S3 bucket with CloudTrail logging functions
      3. Encrypt data stored in a S3 bucket using an encryption key
      4. Monitor encryption key usage using CloudTrail
      5. Manage encryption keys for users and roles
