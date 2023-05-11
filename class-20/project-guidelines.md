# Ops 401 Midterm Project Guidelines

## Scenario & Problem Domain

Your team has been contracted to improve the cybersecurity processes and systems for a client company, focusing on logging, monitoring and detection of adversarial activity on cloud infrastructure.

## Project Requirements

For this project, your client has requested a demonstration of how you'll be able to protect their cloud infrastructure. You'll need to implement the following in AWS Cloud to demonstrate how you'll secure the AWS environment:

- **IAM**
  - Proper IAM best practices must be implemented for the root account
  - Proper IAM for all team members must be implemented using AWS best practices

- **Server Hardening and Data Protection**
  - CIS-compliant Windows Server DC hosted on a private subnet of a VPC and accessible only via VPN tunneling
    - Data needs to be encrypted at rest and encrypted in transit
    - Deploy Sysmon to generate security-relevant system logs
  - CIS-compliant Data Server
    - Linux server instance containing PII and PCI data
    - Data needs to be encrypted at rest and in transit

- **SIEM / Log aggregation system**
  - Splunk, CloudWatch, Elastic Stack
  - Configured to ingest event logs in real time from key assets including EC2 instances
  - Show an attack TTP, attack must incorporate a Python script using a new library you have not worked with yet.
  - The attack should trigger an event that gets ingested by the SIEM solution

- **Cloud Monitoring**
  - Capture traffic for the client to demonstrate how the attack TTPs would be detected in the AWS Cloud using VPC Flow Logs and any additional automation necessary
  - An AWS Lambda function triggering a relevant response to a detected threat (this fulfills the requirement for a shell script)
  - Monitor for threat activity in your AWS environment
  - Monitor Security Logs for failed SSH attempts on your instances

- **Novelty**
  - Challenge yourselves to implement a novel tool, system, or technique that was not demonstrated or performed during lab time in term 1 of your Ops 401 class.

## Assignments & Deliverables

Keep an eye on Canvas for assignments due this week.

- Remember to complete nightly Project Report assignments. These assignments are easy to forget as you get swept up in interesting project subject matter.
- Necessities such as team agreement (conflict resolution, etc.) and project plan will be created in your Project Prep assignments. Instructor approval is required before progressing to the next Project Prep assignment.
- By demo day, you'll need these deliverables assembled:
  - Demo day slide deck
  - Project report
  - Project plan
  - GitHub repo
  - Google drive docs (if used)
- Track your individual contributions throughout the project so that you can easily submit your individual contributions writeup on demo day for grading.

## Standup

Every day, the instructional team with circulate to your group for a formal "Standup Meeting". Standup should take approximately 10 minutes per team. Some instructors will opt for a "retro" later in the day to review how things went.

> Standups give the instructional team insight into the current status of your project and the progress the team hopes to make each day.

During standup, each team member will address these three points:

  1. What you individually accomplished yesterday
  1. What you individually plan to accomplish today
  1. Anything that is blocking you from making progress

## Presentation Prep

Your team will practice your presentation prior to the final presentation day. This is typically scheduled by the instructional team. During the practice presentation, the instructional team will provide constructive feedback about the flow of the presentation and delivery of the subject matter.

Practice and prepare your technical demonstrations in advance of demo day to rule out any quirks/bugs.

General slide deck guidelines:

- The presentation slides must use the aesthetic formatting of the [template slide deck](https://docs.google.com/presentation/d/1iv8uB6H0P49RN9IF6cYA5lpfiuL4WBGQqcbEu6Q4JAA/edit#slide=id.g2accd1c413_1_55).
  - Remember to create your own copy of the template and do not edit the template itself.
- Ensure your timing is no more than 25 minutes long, including some time at the end for questions.
- Present from the final product, deployed site, or official documentation that you produce.
- Each member should introduce themselves with their personal pitch.
  - The "About Us" page provides a great backdrop for this portion of the presentation.

Each member of the team must have a speaking part. It is okay to use presenter notes/outlines but remember to avoid reading notes verbatim and to present naturally as if speaking to a colleague.

The appropriate dress code is business casual - not too formal and not too casual.

Be cognizant of the environment you're presenting from. A clean backdrop, good lighting, and quality mic and webcam go a long ways.

In addition to the scheduled practice session, the team is encouraged to continue to practice on their own. Keep track of the time and adjust accordingly. Practice transitioning speaking segments.

Speak clearly and do not use slang or profanity. Take it seriously and be professional.

> Tip: Slides should be composed of talking points, not lines to be read verbatim! Avoid the "teleprompter" effect and aim for a natural, extemporaneous presentation on demo day.

## Grading

Each team member's grade is split between their individual effort, and the project's technical merit.

Individual effort is graded based on contributions to project deliverables, and professionalism in the presentation.

Technical merit of the project overall is evaluated according the requirements. The Project Grade is a combination of the Presentation (55%) and the Deliverables (45%)

### Presentation (55%)

Components of the presentation must include:

- A. Team members individually introduce themselves using their own professional pitch. (3 min, explain why they are making the career change)
- B. Topical overview (2 min)
  - B1. As the "Problem Domain", describe the project scenario you were assigned and the overall client requirements.
    - B1a. Compliance requirements
    - B1b. Security systems requirements
- C. Technical demonstrations of solutions (12 min)
  - C1. Introduce the cloud architecture diagram of your environment
  - C2. Demonstrate your solution(s) to the problem domain here
- D. Final thoughts on how the project went (3 min)
  - D1. Each team member should share some final thoughts on the project. Some topics you could discuss here include:
    - D1a. The team's approach to planning and communication throughout the project
    - D1b. A technical obstacle or two and how those obstacles were overcome
    - D1c. A portion of the outcome you are particularly proud of achieving
- E. Q&A (5 min)

### Deliverables (45%)

Submit to instructor a single link to your Github Org. All team members are to contribute an equal share to documentation corresponding to the components they worked on and should clearly indicate which components each contributed to in their individual project submission notes.

- **GitHub Repository (10%)**
  - A repo under an appropriately name Github "Organization"
  - Sufficient documentation in the top level README to explain to a stranger who you are, what this project was about, and how all of the material in the repo pertains to it.
    - This README should be:
      - Attractively formatted
      - Include links to relevant files in the repo
      - Include links to each of your own Github accounts AND LinkedIn accounts
  - All other deliverables should be included as files in this repo
  - Deployment scripts: Scripts used to automate the deployment process of the project, which includes provisioning the required AWS resources, deploying the code, and configuring the services.
- **Presentation Material (5%)**
  - Slide deck, as a PDF
  - A link to the video of your presentation (when it becomes available)
- **Cloud Architecture design (20%)**
  - AWS infrastructure components, their interactions, and how they fit together.
    - This diagram should be comprehensive and understandable to all stakeholders involved in the project.
  - All components must be labeled, and diagram must be presentable (straight lines) and free of defects/typographical issues. Take your time to create a quality diagram; do not rush!
  - Clearly indicate AWS instances, networks, tools and services.
  - A clear, written explanation and justification of your cloud architecture design.
  - Add descriptions of how you incorporated these systems into your technical demo:
    - AWS IAM
    - AWS CloudTrail
    - Amazon GuardDuty
  - Include a table or chart of network infrastructure and configuration details (yes, this will overlap with your topology -- you must document your network in both ways):
    - Subnets and their uses
    - Include Subnet Masks, CIDR addresses, etc.
    - Security Group rules
- **SOP and Policy Documentation (10%)**
  - Security Incident Plan
    - The test plan should include detailed testing procedures of security controls and monitoring solutions along with expected outcomes.
    - Include a diagram of the expected events when an attack triggers your monitoring tools.
  - Compliance Documentation
    - Compliance documentation should be developed to demonstrate that the system meets any relevant regulatory requirements.
    - This may include documentation showing compliance with PCI, GDPR, or other industry-specific regulations. (Pick one compliance framework)

## Resources

- Use [Stratus Red Team](https://github.com/DataDog/stratus-red-team) for threat emulation
