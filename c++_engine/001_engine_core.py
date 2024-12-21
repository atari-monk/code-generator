import os

# Create directories for the project structure
directories = [
    "Engine", "Engine/Interfaces", "Engine/Systems"
]

# Create the directories
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Define the contents of the header files and cpp files
files = {
    "Engine/Interfaces/IUpdateable.h": '''#pragma once

class IUpdateable {
public:
    virtual void Update(float deltaTime) = 0;
    virtual ~IUpdateable() = default;
};
''',

    "Engine/Interfaces/IRenderable.h": '''#pragma once

class IRenderable {
public:
    virtual void Render() = 0;
    virtual ~IRenderable() = default;
};
''',

    "Engine/Interfaces/IInputHandler.h": '''#pragma once

class IInputHandler {
public:
    virtual void HandleInput() = 0;
    virtual ~IInputHandler() = default;
};
''',

    "Engine/GameLoop.h": '''#pragma once

#include <memory>
#include "Interfaces/IUpdateable.h"
#include "Interfaces/IRenderable.h"
#include "Interfaces/IInputHandler.h"

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
''',

    "Engine/Systems/GameUpdater.h": '''#pragma once

#include "Interfaces/IUpdateable.h"

class GameUpdater : public IUpdateable {
public:
    void Update(float deltaTime) override;
};
''',

    "Engine/Systems/GameRenderer.h": '''#pragma once

#include "Interfaces/IRenderable.h"

class GameRenderer : public IRenderable {
public:
    void Render() override;
};
''',

    "Engine/Systems/GameInputHandler.h": '''#pragma once

#include "Interfaces/IInputHandler.h"

class GameInputHandler : public IInputHandler {
public:
    void HandleInput() override;
};
''',

    "Engine/Engine.h": '''#pragma once

#include <memory>
#include "GameLoop.h"
#include "Systems/GameUpdater.h"
#include "Systems/GameRenderer.h"
#include "Systems/GameInputHandler.h"

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
''',

    "Engine/Main.cpp": '''#include "Engine.h"

int main() {
    Engine engine;
    engine.Start();
    // engine.Stop(); // Call when you want to stop the engine
    return 0;
}
''',

    "Engine/GameLoop.cpp": '''#include "GameLoop.h"
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
''',

    "Engine/Systems/GameUpdater.cpp": '''#include "GameUpdater.h"
#include <iostream>

void GameUpdater::Update(float deltaTime) {
    std::cout << "Updating game logic with delta time: " << deltaTime << std::endl;
    // Game logic update (physics, AI, etc.)
}
''',

    "Engine/Systems/GameRenderer.cpp": '''#include "GameRenderer.h"
#include <iostream>

void GameRenderer::Render() {
    std::cout << "Rendering scene..." << std::endl;
    // Rendering logic (OpenGL, DirectX, etc.)
}
''',

    "Engine/Systems/GameInputHandler.cpp": '''#include "GameInputHandler.h"
#include <iostream>

void GameInputHandler::HandleInput() {
    std::cout << "Handling input..." << std::endl;
    // Input handling (keyboard, mouse, etc.)
}
''',

    "Engine/Engine.cpp": '''#include "Engine.h"

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
''',

    # CMakeLists.txt
    "Engine/CMakeLists.txt": '''# Set the minimum version of CMake required
cmake_minimum_required(VERSION 3.10)

# Define the project name
project(GameEngine)

# Set the C++ standard (e.g., C++17)
set(CMAKE_CXX_STANDARD 17)

# Add the source files (the .cpp files in the Systems and root folder)
set(SOURCES
    Engine/Main.cpp
    Engine/GameLoop.cpp
    Engine/Systems/GameUpdater.cpp
    Engine/Systems/GameRenderer.cpp
    Engine/Systems/GameInputHandler.cpp
    Engine/Engine.cpp
)

# Add the include directories (for header files)
include_directories(Engine/Interfaces)

# Add the executable
add_executable(GameEngine ${SOURCES})

# If using any external libraries, you can link them here:
# target_link_libraries(GameEngine <library_name>)
'''
}

# Write the content to files
for file_path, content in files.items():
    with open(file_path, "w") as file:
        file.write(content)

print("C++ project structure has been generated, including CMakeLists.txt!")
