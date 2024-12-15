---
layout: default
title: "Algorithms and Data Structures Enhancement"
---

# Algorithms and Data Structures Enhancement

<iframe width="560" height="315" src="https://www.youtube.com/embed/ULhIkaCrTUU" frameborder="0" allowfullscreen></iframe>

For this enhancement, I continued with my IT 140 text-based game called House Cleaning Adventure. I created it almost two years ago in my first Python course at SNHU. Today for this section of the artifact enhancement I included this artifact in my ePortfolio because I felt for my current interests, I would be able to enhance this artifact throughout the course for each category of enhancements to be made while fulfilling all of our course outcomes. It also played a role in that this being one of my first projects in the CS program at SNHU it would best showcase how much I have improved throughout the program. This artifact will best present my ability to enhance my existing code and apply new technologies that I did not originally use like Pygame to improve the overall user experience of the game.

While developing my plan for this capstone project I saw the potential of this artifact to showcase my ability to apply advanced algorithms and data structures within a game environment. Specific areas that I enhanced in this artifact are adding an AI agent (child dirtying the house) this was through using a pathfinding algorithm to enhance the complexity and interactivity of the House Cleaning adventures. To do this I represented the rooms and their connections as a graph data structure, where rooms are nodes, and connections are edges. 
 
 Next, I added an agent.py to keep with the modularity of the project. My goal here was to implement A* instead of my original idea of BFS to traverse the graph structure. After attempting BFS and not liking the outcome I switched to A* and implemented the Agent class
 
I implemented the A* algorithm within our utils.py along with the heuristic to help the agent weigh which rooms to dirty. 
 
I have also included a video at the top of the document to showcase the enhancements working together.  It was truly fun to work and figure out the nuances of getting this algorithm to work the way I intended it to within the House Cleaning Adventure game. I have completed the course outcome for this enhancement by implementing A*. While I still have more feedback to implement along the way, enhancing this has become a great joy. The biggest learning moment this week is realizing sometimes the best-laid plans do not always work out the way you want. In this case, I was able to explore more of A* and heuristic which I am thankful for. The challenges of implementing it and getting the agent to behave the way I wanted were tricky but were solved by implementing a wait before the agent began cleaning. I am looking forward to implementing more of the feedback and adding a database base to this game.

**Key Changes:**
- Implemented A* pathfinding for the agent to intelligently navigate rooms.
- Represented rooms and connections as a graph structure for effective traversal.
- Moved from a simpler BFS approach to a more efficient heuristic-driven algorithm.
- Implemented agent's "wait threshold" mechanic to add genuine challenge to the gameplay

**Link to Relevant Code:**
[Agent and Pathfinding Logic](https://github.com/briggs8933/CS-499-Capstone/blob/main/Enhanced%20House%20Cleaning%20Adventure/agent.py)

**Outcome Alignment:**
- **Outcome 3:** A* pathfinding exemplifies designing and evaluating computing solutions using sound algorithmic principles, managing complexity and performance trade-offs.
- **Outcome 4:** Employing a well-regarded algorithm and data structures reflects innovative, value-oriented computational techniques.

**Reflections:**
Switching from BFS to A* broadened my understanding of heuristic-driven algorithms. Although challenging, the adaptation improved my problem-solving skills and highlighted the importance of choosing the right approach to achieve the desired functionality and efficiency.
