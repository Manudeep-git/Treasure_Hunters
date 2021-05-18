## EECS 738 Project 4: Reinforcement Learning

### Overview

The purpose of this project is to implement a reinforcement learning policy to model situational assessments, actions, and rewards programmatically. Multiple two-dimensional maze-like environments with goals/treasures (yellow squares), walls (black squares), and enemies (red squares) were created to test the agent (green square). Q-learning was implemented to teach the agent how to quickly obtain treasures and avoid enemies. The amount of time taken to collect all treasures and the number of enemies fought served as metrics to gauge the performance of the agent. GIFs were created for each environment to easily illustrate the agent's behavior and the efficacy of the training algorithm.

### Approach

First, the two-dimensional maze-like environments and visualization tools were created using NumPy arrays and a library called array2gif. As soon as GIFs could be created to show the movement of an agent on a two-dimensional plane, simple mazes were created with no obstacles or enemies. The initial mazes contained only the agent and a single treasure. Then, Q-learning was used to produce a path that would lead the agent directly to the treasure. This was accomplished by giving the agent a small negative reward, or penalty, for every step taken. This was included to ensure that direct paths were taken to treasures. To indicate the yellow squares were desirable, a large positive reward was given to the agent whenever it moved to a cell containing a treasure.

Once this was accomplished, larger environments were created with walls and multiple treasures. Walls served as impassable boundaries preventing the agent from moving directly to a treasure. After the agent could avoid these obstacles and collect multiple treasures, enemies were introduced. Unlike walls, the agent could move into, or attack, these enemies. However, attacking enemies resulted in a moderate negative reward, or penalty. Doing this incentivized the agent to generally avoid enemies and attack if necessary. One can think of the agent as a pacifist. A notable test performed involved a long winding path to a treasure with no enemies and a short path directly to a treasure with one enemy. The penalties were set such that attacking this enemy and traveling directly to the treasure resulted in a lower overall cost than traversing the enemy-free path. This example illustrates the agent's dynamic learned decision-making capabilities.

### How to Run

This project was written in Python 3.9.4 and required modules can be installed by navigating to the project directory and running this below command:
```
pip3 install -r requirements.txt
```
Once the dependencies are installed, learning can start. To train an agent, an environment size must be specified. The available sizes are "small", "medium", and "large". Optionally, the presence of enemies in each environment can be toggled by adding "enemies" to the command. Each of the environments can used by issuing a command of this format:
```
python main.py <size> [enemies]
```

**Examples:**

To run the small environment with no enemies:
```
python main.py small
```

To run the medium environment with enemies:
```
python main.py medium enemies
```

**Note: It takes a very long time to train on the large environment without enemies. This has already been done and the results are shown below**

### Results

For each environment, a GIF and plot were created. The GIF graphically shows the agents path through the environment. The plot shows the number of time steps taken to collect all treasures at each episode during training. There is a general trend in each plot. They all start rather high (it takes a long time to collect all treasures initially because the agent hasn't learned how), and as training continues, the amount of time steps taken to collect all treasures decreases and eventually converges as the model learns the best path. Plots were not included for the small environments since they were so simple. Essentially no improvement was shown in the small plots.

**Note: In these examples the green square represents the agent, yellow squares represent treasure, black squares represent walls, and red squares represent enemies**

**Small environment with no enemies:**

![](https://i.imgur.com/FdjkZI7.gif)

With no enemies or obstacles, the agent maximizes its reward by heading directly for each treasure.

**Small environment with enemies:**

![](https://i.imgur.com/8RNZwcU.gif)

To avoid the moderate penalty of fighting, the agent circumvents the enemies to collect the treasures. In this basic example, the agent essentially treats the enemies as walls. The penalty for attacking the enemies is much higher than the penalty for the few steps it takes to avoid them.

**Note: I am not including the medium mazes over here , but these simulations/animations can be found <a href='./animations/medium.gif'>here</a> and <a href='./animations/medium_enemies.gif'>here</a>** 

**Large environment with no enemies:**

![](https://i.imgur.com/nZ3rZn4.gif)

Clearly, this environment takes inspiration from Pac Man. As opposed to the medium environment with no enemies, this environment contains multiple paths to each treasure, which greatly expands the state and solution spaces. This test was meant to stress-test the capabilities of the Q-learning implementation.

![](https://i.imgur.com/KkyQ4Wr.png)

This plot shares the trend that each of the previous plots possess. Over time, the agent becomes more adept at collecting all treasures in a timely manner. Something worth noting is the much higher number of episodes required for the number of time steps to converge. This is a direct consequence of the incredibly large state and solution space.

**Large environment with enemies:**

![](https://i.imgur.com/Ch7Zisb.gif)

This final environment illustrates an interesting phenomenon. In the small environment with enemies, the agent treated the enemies as walls because it could. In that example there was another path around the enemies. In the medium environment with enemies, the agent only attacked the enemy because it was the only way to obtain the final treasure. In this example, there is clearly a path around the enemy that leads to all treasures. However, the agent attacks. This is because of the factors driving the agent. As previously stated, the agent is trying to *quickly* collect all of the treasures while simultaneously avoiding enemies. Because the path around the enemy is so long, the penalty for taking that path is much higher than the penalty for attacking the enemy. The agent chooses to attack the enemy in order to collect the treasures in a short amount of time.

![](https://i.imgur.com/MNlHPDn.png)

This plot converged faster than any other environment. This is simply because the resulting (best) path was so simple. After only about 10 episodes, the agent learned that attacking the enemy and heading straight for the treasures was faster than going around the enemy. It's worth noting the incredibly large number of time steps the agent initially took per episode to avoid attacking the enemy before finding out attacking the enemy resulted in a lower overall penalty.

### Optimizations and Future Work

I think future would work be implementing multiple reinforcement learning algorithms and compare the results. Perhaps one algorithm would have found the best solution faster than all others for this application. Another piece of future work would be making the enemies move or chase the agent.Also, Training a model in an environment with moving enemies soon becomes infeasible due to the incredible number of possible states. Further improvements could also be made to the current Q-learning implementation to reduce total execution time, such as hyperparameter tuning or general architecture redesign. Also, the dimensionality of the environments can be expanded. As it stands, the algorithm should be able to support this with minimal changes.
