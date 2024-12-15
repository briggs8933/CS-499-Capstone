---
layout: default
title: "Database Enhancement"
---

# Database Enhancement

<iframe width="560" height="315" src="https://www.youtube.com/embed/SmAEqfFRv84" frameborder="0" allowfullscreen></iframe>


For our last enhancement, I continued with my IT 140 text-based game called House Cleaning Adventure. I created it almost two years ago in my first Python course at SNHU. For this section of the artifact enhancement, I included this artifact in my ePortfolio because I felt that, given my current interests, I would be able to enhance this artifact throughout the course for each category of enhancements to be made while fulfilling all our course outcomes. Additionally, being one of my first projects in the CS program at SNHU, it would best showcase how much I have improved throughout the program. This artifact will best present my ability to enhance my existing code and apply new technologies that I did not originally use, such as Pygame, to improve the overall user experience of the game.

This enhancement, adding a database, showcases my ability to refactor my code to include database integration. The specific components that were improved to showcase my skills included adding a database.py to our already modular code and expanding and refactoring different classes within the game to accommodate the addition of the database. This included creating a database schema to hold all our old data (rooms, room connections, clean/dirty status) and our new data (player username/login, agent tracking, and game results data like high scores and win/lose records). With these additions, I have a working House Cleaning Adventure that stores, manipulates, and accesses data from the database within the game loop to create a unique experience compared to the original text-based game.

When looking to meet the course outcomes for this part of the enhancement, I was able to complete the expected course outcomes of 3, 4, and 5. In my original plan, I had reserved course outcome 3 specifically for our last milestone. There was a particular amount of effort put into getting the database to work with everything that had already been implemented from the original and the last two milestones.

Reflecting on the process brings me both pain and joy. I am beginning to feel the effects of how ambitious these enhancements were, and it has taught me that my planning could always be better. I could have more patience with my work, and lastly, you cannot implement every idea you have. There will be time in the future for the things that didn’t make the cut. On the bright side, my knowledge of using SQLite within Python has expanded tremendously, as well as revisiting older topics like creating login pages. It reminds me of all the classes throughout the program, and it was nice to revisit many of those older projects for insight.



**Key Changes:**
- Implemented a SQLite database for persistent data storage.
- Created a `database.py` module and adapted classes to interact seamlessly with the database.
- Added user authentication with password hashing, secure input validation, and high score tracking.

**Link to Database Code:**
[Database Integration Code](https://github.com/briggs8933/CS-499-Capstone/blob/main/Enhanced%20House%20Cleaning%20Adventure/database.py)

**Outcome Alignment:**
- **Outcome 3:** Integrating the database required careful architectural decisions and managing evolving requirements.
- **Outcome 4:** Using SQLite and secure coding practices shows employing well-founded tools for delivering industry-specific value.
- **Outcome 5:** Anticipating vulnerabilities and ensuring data privacy demonstrates a proactive security mindset.

**Reflections:**
Though ambitious, this enhancement deepened my understanding of persistent storage, user management, and secure coding. Revisiting concepts like login systems linked past learnings into a cohesive skill set, making this artifact a comprehensive demonstration of my development as a computing professional.
