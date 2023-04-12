# Interview Demo

This will be used as an in-class demonstration of how the mock interview process should work. The below topic was pulled from Ops 301. In a technical job interview, be prepared for anything. You will likely be tested at multiple levels of comprehension: "What is it, why is it important, and how does it work?" Foundational concepts such as the IP stack are fair game in this industry. The below is an example of a common interview question at the entry level, designed to assess your comprehension of computer networking and how security needs correlate. 

Mock interview questions in this class, however, will generally align with the subject matter introduce the same week.

## Interview Question

Ask the candidate: 
- What is a three-way handshake and how does it work? 
  - Please illustrate the process using a screenshare and drawing tool of your choosing.
- What protocol is used?
- What type of connection is this, one-way or two-way, and what is the technical term for that?
- Why should security professionals know how this works?

## Interviewer Notes

Key areas to explore and discuss:
- A three-way handshake is a method used in a TCP/IP network to create a connection between a host and a client. It’s called a three-way handshake because it is a three-step method in which the client and server exchanges packets. The three steps are as follows:
  - The client sends a SYN (synchronize) packet to the server check if the server is up or has open ports
  - The server sends SYN-ACK packet to the client if it has open ports
  - The client acknowledges this and sends an ACK (acknowledgment) packet back to the server, and the connection is established.
- The three-way handshake uses the TCP protocol. 
- This is a duplex (two-way traffic) connection.
- The three-way handshake can be exploited in a number of ways, for example by a flood attack.  Specially-crafted packets at a high volume can overwhelm the server and cause denial of service.

## Preparation

Before the interview:
- Carefully review the interview question and interviewer notes.
- Create your own copy of [interview grading rubric](https://docs.google.com/spreadsheets/d/1scthkmARfzAFZrSYAp6LA2coOaoWUWbSzMbtIU4jcHw/edit)
- Fill in the details at the top, such as Student and Interviewer
- Familiarize yourself with the grading rubric, so you know how to score the interview. Review the criteria in advance of the interview so you can steer the conversation towards the scoring requirements.

## During the Interview

- Act as an interviewer, giving a candidate the interview question(s)
- Score the candidate according to the rubric
  - Assign points for each item on the rubric, according to how well the candidate executed on that skill.
- You are free to offer suggestions or guidance (and see how they respond),  but don't solve it for the candidate.
- Every solution might look and sound a little different, but the candidate should be able to verify their solution with different edge cases to verify correctness. The candidate should NOT be reading notes verbatim; instead, quesitions should be answered as authentically as possible.

## After the interview

- Add up all the points at the end, and record the total at the bottom of the page. Include a photo or screenshot of their whiteboard.
- Record detailed notes on the rubric, to share with the candidate when the interview is complete.
