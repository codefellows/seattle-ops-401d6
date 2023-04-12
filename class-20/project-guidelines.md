# Ops 401 Midterm Project Guidelines

## Scenario & Problem Domain

Your team has been contracted to improve the cybersecurity processes and systems for a client company.

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
- The presentation slides must use the aesthetic formatting of the [template slide deck](https://docs.google.com/presentation/d/16LOH5KiIVGq3oJReWa2kVO_VgQZlYG9K4vNXJuJNJdE).
  - Remember to create your own copy of the template and do not edit the template itself.
- Ensure your timing is no more than 25 minutes long, including some time at the end for questions.
- Present from the final product, deployed site, or official documentation that you produce.
- Each member should introduce themselves with their personal pitch.
  - The "About Us" page provides a great backdrop for this portion of the presentation.

Each member of the team must have a speaking part. It is okay to use presenter notes/outlines but remember to avoid reading notes verbatim and to present naturally as if speaking to a colleague.

Components of the presentation must include:

- A. Team members individually introduce themselves using their own professional pitch. (3 min, explain why they are making the career change)
- B. Topical overview (2 min)
  - B1. As the "Problem Domain", describe the project scenario you were assigned and the overall client requirements.
    - B1a. Compliance requirements
    - B1b. Security systems requirements
- C. Technical demonstrations of solutions (12 min)
  - C1. Introduce the network topology of your environment
  - C2. Demonstrate your solution(s) to the problem domain here
- D. Final thoughts on how the project went (3 min)
  - D1. Each team member should share some final thoughts on the project. Some topics you could discuss here include:
    - D1a. The team's approach to planning and communication throughout the project
    - D1b. A technical obstacle or two and how those obstacles were overcome
    - D1c. A portion of the outcome you are particularly proud of achieving
- E. Q&A (5 min)

The appropriate dress code is business casual - not too formal and not too casual.

Be cognizant of the environment you're presenting from. A clean backdrop, good lighting, and quality mic and webcam go a long ways.

In addition to the scheduled practice session, the team is encouraged to continue to practice on their own. Keep track of the time and adjust accordingly. Practice transitioning speaking segments.

Speak clearly and do not use slang or profanity. Take it seriously and be professional.

> Tip: Slides should be composed of talking points, not lines to be read verbatim! Avoid the "teleprompter" effect and aim for a natural, extemporaneous presentation on demo day.

## Grading

Each team member's grade is split between their individual effort, and the project's technical merit.

Individual effort is graded based on contributions to project deliverables, and professionalism in the presentation.

Technical merit of the project overall is evaluated according the requirements.

### Deliverables

Submit to instructor a single "Project Report" Google Doc. All team members are to contribute an equal share to documentation corresponding to the components they worked on and should clearly indicate which components each contributed to in their individual project submission notes.

Teams are encouraged to adopt an Agile mindset with regards to the development of their project deliverables and regularly solicit feedback from staff regarding their project report, slide deck, and other deliverables. The quality of your reporting will be evaluated and will directly impact the group submission grade. Remember to budget adequate time and attention for project deliverables to ensure a high quality of work is delivered. The client point of contact should be contacted via email regarding scenario-specific scoping.

Here is a list of requirements your manager would like to see addressed in your final project report:

- Preparation
  - Obtain the Network Security Assessment from your instructor and analyze the findings.
- PD01: Risk Assessment Worksheet
  - Complete a risk assessment worksheet for your client company, addressing threats to the company's operations and what level of risk they each present.
- PD02: Security Assessment Report (SAR)
  - Using the [SAR template file](https://www.icloud.com/iclouddrive/0mLh-le4fAPK-j24pJTmYzOsg#sar-template-v2), complete a SAR.
  - Include and discuss the findings of your risk assessment worksheet.
- PD03: Data Security Policy
  - Using the [data security policy template](https://www.icloud.com/iclouddrive/02ASEYZEy9ynPM3ph6Zw8YoJg#Data_Security_Policy_Template), complete a data security policy that addresses data security concerns such as encryption and DLP practices.
  - Mention any relevant systems you've implemented.
- PD04: Cloud Security Policy
  - Using the Class 02 template file, create a cloud security policy for your client.
- PD05: Security Architecture Narrative
  - Using the Class 01 template file, create a security architecture narrative for your client.
  - Create and include a cloud topology of your environment using a tool such as draw.io. Keep in mind that a cloud topology differs from a traditional LAN, so use the correct icons and structure appropriate to what you're depicting.
  - Add descriptions of how you incorporated these systems into your technical demo:
    - AWS IAM
    - AWS CloudTrail
    - Amazon GuardDuty
  - Exclude the Physical Security section.
  - Explain how CIS benchmarks were incorporated into your Windows deployment(s) in the cloud. Validate CIS compliance using AWS Security Hub.
    - Explain how FDE was used to secure hard drives on your systems.
    - Explain how PKI was used in your cloud environment.

### Resources

Reference the below resources for developing your security assessment report.

- [Tips for Creating a Strong Cybersecurity Assessment Report](https://zeltser.com/security-assessment-report-cheat-sheet/)
- [CMS Security Assessment Report Template](https://www.cms.gov/Research-Statistics-Data-and-Systems/CMS-Information-Technology/InformationSecurity/Downloads/Security-Assessment-Report-Template.docx)
- [Security Assessment Report Example](https://www.silabs.com/documents/public/white-papers/SP02508-Sigma-Designs-Security2-Command-Class_v2_Commercial_in_Confidence_Removed.pdf)

Reference the below resources for developing your STRIDE/DREAD analysis.

- [Qualitative Risk Analysis with the DREAD Model](https://resources.infosecinstitute.com/qualitative-risk-analysis-dread-model/)
- [STRIDE/DREAD Analysis: Threat Modeling of Trinity Wallet Example](https://files.iota.org/trinity/Threat+Modelling+Report+V1.2.signed.pdf)

Reference the below resources for developing your threat model technical report.

- [Enterprise Threat Model Technical Report Example](https://www.mitre.org/sites/default/files/publications/pr_18-1613-ngci-enterprise-threat-model-technical-report.pdf)

Reference the below resources for developing your NOC/SOC SOP.

- [Guideline to Develop and Maintain the Security Operation Center (SOC)](https://resources.infosecinstitute.com/guideline-to-develop-and-maintain-the-security-operation-center-soc/)
- [NIST Risk Management Framework Overview](https://www.nist.gov/system/files/documents/2018/03/28/vickie_nist_risk_management_framework_overview-hpc.pdf)
