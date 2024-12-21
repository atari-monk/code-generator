# Engine Core

To generate fast use script

[script](001_engine_core.py)

Details to read:

## 1. **IUpdateable.h** (Interface for updating)

```cpp
#pragma once

class IUpdateable {
public:
    virtual void Update(float deltaTime) = 0;
    virtual ~IUpdateable() = default;
};
```

## 2. **IRenderable.h** (Interface for rendering)

```cpp
#pragma once

class IRenderable {
public:
    virtual void Render() = 0;
    virtual ~IRenderable() = default;
};
```

## 3. **IInputHandler.h** (Interface for input handling)

```cpp
#pragma once

class IInputHandler {
public:
    virtual void HandleInput() = 0;
    virtual ~IInputHandler() = default;
};
```

## 4. **GameLoop.h** (Main loop class)

```cpp
#pragma once

#include <memory>
#include "IUpdateable.h"
#include "IRenderable.h"
#include "IInputHandler.h"

class GameLoop {
public:
    GameLoop(std::shared_ptr<IUpdateable> updater,
             std::shared_ptr<IRenderable> renderer,
             std::shared_ptr<IInputHandler> inputHandler);

    void Run();
    void Stop();

private:
    bool m_isRunning;
    std::shared_ptr<IUpdateable> m_updater;
    std::shared_ptr<IRenderable> m_renderer;
    std::shared_ptr<IInputHandler> m_inputHandler;
};
```

## 5. **GameUpdater.h** (Concrete update class)

```cpp
#pragma once

#include "IUpdateable.h"

class GameUpdater : public IUpdateable {
public:
    void Update(float deltaTime) override;
};
```

## 6. **GameRenderer.h** (Concrete renderer class)

```cpp
#pragma once

#include "IRenderable.h"

class GameRenderer : public IRenderable {
public:
    void Render() override;
};
```

## 7. **GameInputHandler.h** (Concrete input handler class)

```cpp
#pragma once

#include "IInputHandler.h"

class GameInputHandler : public IInputHandler {
public:
    void HandleInput() override;
};
```

## 8. **Engine.h** (Engine class that sets up and manages the game loop)

```cpp
#pragma once

#include <memory>
#include "GameLoop.h"
#include "GameUpdater.h"
#include "GameRenderer.h"
#include "GameInputHandler.h"

class Engine {
public:
    Engine();
    void Start();
    void Stop();

private:
    std::shared_ptr<IUpdateable> m_updater;
    std::shared_ptr<IRenderable> m_renderer;
    std::shared_ptr<IInputHandler> m_inputHandler;
    std::unique_ptr<GameLoop> m_gameLoop;
};
```

## 9. **Main.cpp** (Main file for execution)

```cpp
#include "Engine.h"

int main() {
    Engine engine;
    engine.Start();
    // engine.Stop(); // Call when you want to stop the engine
    return 0;
}
```

## 10. **GameLoop.cpp** (Implementation of the GameLoop class)

```cpp
#include "GameLoop.h"
#include <iostream>
#include <chrono>
#include <thread>

GameLoop::GameLoop(std::shared_ptr<IUpdateable> updater,
                   std::shared_ptr<IRenderable> renderer,
                   std::shared_ptr<IInputHandler> inputHandler)
    : m_updater(updater), m_renderer(renderer), m_inputHandler(inputHandler), m_isRunning(true) {}

void GameLoop::Run() {
    auto previousTime = std::chrono::high_resolution_clock::now();

    while (m_isRunning) {
        // Time step calculation
        auto currentTime = std::chrono::high_resolution_clock::now();
        std::chrono::duration<float> deltaTime = currentTime - previousTime;
        previousTime = currentTime;

        float deltaSeconds = deltaTime.count();

        // Handle input, update game state, and render
        m_inputHandler->HandleInput();
        m_updater->Update(deltaSeconds);
        m_renderer->Render();

        // Sleep to control framerate
        std::this_thread::sleep_for(std::chrono::milliseconds(16)); // ~60fps
    }
}

void GameLoop::Stop() {
    m_isRunning = false;
}
```

## 11. **GameUpdater.cpp** (Implementation of the GameUpdater class)

```cpp
#include "GameUpdater.h"
#include <iostream>

void GameUpdater::Update(float deltaTime) {
    std::cout << "Updating game logic with delta time: " << deltaTime << std::endl;
    // Game logic update (physics, AI, etc.)
}
```

## 12. **GameRenderer.cpp** (Implementation of the GameRenderer class)

```cpp
#include "GameRenderer.h"
#include <iostream>

void GameRenderer::Render() {
    std::cout << "Rendering scene..." << std::endl;
    // Rendering logic (OpenGL, DirectX, etc.)
}
```

## 13. **GameInputHandler.cpp** (Implementation of the GameInputHandler class)

```cpp
#include "GameInputHandler.h"
#include <iostream>

void GameInputHandler::HandleInput() {
    std::cout << "Handling input..." << std::endl;
    // Input handling (keyboard, mouse, etc.)
}
```

## 14. **Engine.cpp** (Implementation of the Engine class)

```cpp
#include "Engine.h"

Engine::Engine() {
    m_updater = std::make_shared<GameUpdater>();
    m_renderer = std::make_shared<GameRenderer>();
    m_inputHandler = std::make_shared<GameInputHandler>();
    m_gameLoop = std::make_unique<GameLoop>(m_updater, m_renderer, m_inputHandler);
}

void Engine::Start() {
    m_gameLoop->Run();
}

void Engine::Stop() {
    m_gameLoop->Stop();
}
```

### How It Works:

-   **Header Files (`.h`)**: These define the interfaces and class declarations. They are included where needed to use the classes or interfaces.
-   **Source Files (`.cpp`)**: These implement the functionality for each class.
-   **Main.cpp**: The entry point for the application that creates the `Engine` and starts the game loop.
