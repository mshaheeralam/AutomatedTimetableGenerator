Automated Timetable Generator

Abstract: Universities, these days have several departments, and each department offers
different degree programs. Each study program has multiple batches enrolled and different 
courses are taught in different programs. There are multiple course instructors, and each 
instructor teaches multiple courses coupled with this is the restriction of having limited 
classrooms. Thus, forming a timetable becomes a very cumbersome and strenuous task. As part 
of our semester project, we intend to solve this problem making the lives of the student, 
instructors, and the administration easier.

1. Introduction

Manual timetable scheduling is a very hectic job. It needs excessive amounts of energy
and time. The problem is quite complex and hence computers were never considered a 
solution. In several state universities, people from the administration are still found on 
the floor with pages and scales and stationary trying to work out a timetable.
The problem does not end here, the timetable generated usually still has clashes 
because humans are error-prone and there are also limitations as to the number of 
classrooms available. The process has to be repeated all over again if an instructor’s 
office hours are changed or he drops or switches a course. 
Therefore, in light of the above-mentioned problematic paradigm, there is a dire need 
to have a tool that aids the process.
Automated Timetable Generator will automate the process of timetable making and will 
eliminate all of the above complications. It will make it easier for the admin as well as 
for students to refrain from facing clashes and can peacefully start their semester 
without any hurdles. And in case of any changes, all one has to do is to rerun the code 
and a completely new timetable will be generated which can be implemented straight 
away. Hence, easing up the revision process too.

2. Formal Problem Statement

Each class of a course is represented as a block (lasts an arbitrary number of hours, 
mostly from 1 to 4). For conducting every class, the following resources are required:
• Teacher
• Classroom
• Start time
• Duration 
• Students which attend the class. 
The students taking the course and the teacher are known in advance. Each classroom
has the same size i.e. each group can fit a hall. Teaching timings are 9 AM till 9 PM on 
each workday (Monday to Friday) i.e. a 60-hour workweek. The class takes place in one 
of the allowed classrooms.
Input data: Details about the above-mentioned resources.
Output data: Time and classroom for each class. Time is fixed by day (Monday to Friday) 
and start hour of the class.

Constraints:
Resources cannot overlap time-wise: • No teacher can hold two classes at the same time
• No group can listen for two classes at the same time
• One classroom cannot have two different classes at the same time.
The solution also attempts to: 
• Minimize total "idle" for each group (eliminating pause between classes)
• Minimize total "idle time" for each teacher (elimination of pause between 
classes)

3. Technology

After a rigorous study of various contenders, it is concluded that the following 
technologies are best suited for our problem:
• Python 
• Django framework for front end and back end
4. Feasibility and Defense of Proposed Technologies
Python:
Python is a multi-paradigm programming language. Object-oriented programming and 
structured programming are fully supported. Python is one of the most versatile 
languages and is used almost everywhere. Following is the gist of Why Python is the 
perfect choice for us: 
• Easy to learn: Python is a significantly easy programing language. Any 
programmer with little experience can learn python.
• Library Support: Python is highly enriched in libraries. Hence, further adding 
functionality and ease to our solution.

Django:
Django is a free and open-source Python framework. It eases the creation of complex, 
database-driven websites. Python is used throughout, even for settings, files, and data 
models. Django also provides an optional administrative create, read, update and delete 
interface.
• Django is not a new platform. It has been around for a while and has been 
quite popular for its reliability. It is very stable particularly in terms of 
security.
• Django is known for its scalability. Django websites can hold a heavy amount 
of traffic and the heaviest amount of data transfer. 

6. Other focus areas

Why is the project compelling and worth developing?
The primary idea of the project surfaced in our minds at the start of our 4th
semester when the timetable was already 3 days late. Once it arrived, it was figured out 
that there were several problems with several classes. To sum it up, it took 3 iterations
to get the perfect timetable. The administration themselves were trying too hard to get 
this task done but given the number of students and the resource limitations, made 
things quite hard for them. Hence, we decided to take our semester project and solve
the problem.

Scope and Target Customers
The target of our product will be all educational institutes be it schools or 
universities. The product is designed keeping universities in mind, however, schools 
follow the same approach. From mid-sized to public universities the product can help all 
universities design a timetable for their students in one go ready to be implemented.
The product is designed while keeping real-world complexities and limitations in 
mind. Hence, scheduling several classes around the campus without resources clashing 
is what this product should primarily do. 

What is novel in our approach?
Such products do exist in the market already, however, the majority of them are 
not able to scale the solutions to universities where the complexities are surreal. We 
intend to take an approach that helps to produce a solution in the complexities of the 
universities. Moreover, none of the products have the scalability as they have not been 
developed in Django. We intend to use Django so that the solution itself does not break 
in case of too much of data.
