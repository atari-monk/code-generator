Step-by-step guide for handling config files in a Python CLI app with best practices:

### 1. **Install `platformdirs` (Optional, for cross-platform support)**

```bash
pip install platformdirs
```

### 2. **Import Required Libraries**

```python
from pathlib import Path
from platformdirs import user_config_dir
```

### 3. **Define the Config Directory**

-   Use `platformdirs` to get the appropriate user config directory.

```python
config_dir = user_config_dir(appname="<AppName>", appauthor="<AuthorName>")
config_path = Path(config_dir) / "config.json"
```

### 4. **Ensure the Directory Exists**

-   Create the config directory if it doesn't exist.

```python
config_path.parent.mkdir(parents=True, exist_ok=True)
```

### 5. **Save Configuration Data**

-   Example of saving data (e.g., JSON) to the config file.

```python
import json

config_data = {"key": "value"}
with open(config_path, "w") as f:
    json.dump(config_data, f, indent=4)
```

### 6. **Load Configuration Data**

-   Example of loading the config data.

```python
with open(config_path, "r") as f:
    config_data = json.load(f)
```

### 7. **Error Handling**

-   Handle cases where the config file might not exist.

```python
try:
    with open(config_path, "r") as f:
        config_data = json.load(f)
except FileNotFoundError:
    config_data = {}  # Default value
```

---

### Summary:

-   Use `platformdirs` for cross-platform directory handling.
-   Store config files in `AppData\Local` (Windows) or equivalent on other OSs.
-   Ensure directories exist before saving data.
-   Use JSON or other formats for storing app data.
