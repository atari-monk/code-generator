# Here’s the **MVP Plan**:

## Core Features for MVP

1. **Map**: A simple top-down map with a parking lot and obstacles.
2. **Car**: A drivable car with basic physics (acceleration, rotation).
3. **Parking Objective**: Highlighted parking spaces where the player needs to park.
4. **Scoring**: Success and failure conditions when parking (e.g., hitting obstacles or parking correctly).

---

## Why Pygame?

-   Easy to set up.
-   Handles 2D graphics and input efficiently.
-   Built-in collision detection and sprite support.

---

## Basic Architecture

1. **Game Engine**: A lightweight loop for handling events, drawing frames, and updating game logic.
2. **Entities**: Car, Parking Lot, Obstacles.
3. **Collision Detection**: Basic rectangle or polygon collision.
4. **Physics**: Simple car movement (forward, backward, rotation).

---

## Next Steps After MVP

1. **Map Design**:

    - Add a background image or grid-based tiles for a parking lot.
    - Introduce static obstacles (like walls or barriers).

2. **Parking Logic**:

    - Define parking zones (rectangles) and detect if the car is inside a zone.
    - Score based on correct parking alignment.

3. **Polish Movement**:

    - Add friction or smoother acceleration.
    - Refine collision detection for obstacles.

4. **UI Elements**:
    - Scoreboard or timer to add challenge.
    - Start and end screens.
