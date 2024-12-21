# Step 1: Prompt for the target directory
$targetDir = Read-Host "Enter the directory where the NX workspace should be created"

# Exit script if no target directory is provided
if (-not $targetDir) {
    Write-Host "No target directory provided. Exiting..."
    exit
}

# Step 2: Ensure the target directory exists
if (-not (Test-Path $targetDir)) {
    Write-Host "Directory $targetDir does not exist. Creating it..."
    New-Item -ItemType Directory -Path $targetDir
}

# Step 3: Prompt for the workspace name
$workspaceName = Read-Host "Enter the workspace name"

# Exit script if no workspace name is provided
if (-not $workspaceName) {
    Write-Host "No workspace name provided. Exiting..."
    exit
}

# Step 4: Check if the workspace already exists in the target directory
if (Test-Path "$targetDir\$workspaceName") {
    Write-Host "Workspace $workspaceName already exists in $targetDir. Exiting..."
    exit
}

# Step 5: Change to the target directory
Set-Location -Path $targetDir
Write-Host "Changing directory to $targetDir..."

# Step 6: Create the NX workspace with the dynamic workspace name
Write-Host "Creating NX workspace $workspaceName..."
npx create-nx-workspace@latest $workspaceName --preset=nest --appName=server --ci=skip --formatter=prettier --e2eTestRunner=none --docker=false

# Step 7: Move into the newly created project directory
Set-Location -Path "$targetDir\$workspaceName"

# Step 8: Install NX plugins as devDependencies
Write-Host "Installing NX plugins as dev dependencies..."
npm install --save-dev @nx/react @nx/js @nx/nest

# Step 9: Generate the necessary apps and libraries
Write-Host "Generating apps and libraries..."
nx generate @nx/react:app apps/client --style=styled-jsx --routing=false --bundler=vite --linter=eslint --unitTestRunner=vitest --e2eTestRunner=none
nx g @nx/nest:library packages/shared-nest
nx generate @nx/js:library packages/shared --style=styled-jsx --linter=eslint --unitTestRunner=vitest --bundler=vite
nx g @nx/react:lib packages/shared-ui --style none --bundler=vite --linter=eslint --unitTestRunner=vitest

Write-Host "Setup completed successfully!"