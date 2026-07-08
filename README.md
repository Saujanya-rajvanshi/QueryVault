To make the invisible parts of a database visible.

## project Architecture 

                 Browser
                    ↓
          React Frontend (Visualization)
                    ↓
            FastAPI Backend
                    ↓
             Query Engine
                    ↓
        Storage Layer (JSON files)

## file structure 

```
QUERYVAULT
|
├── core
|     └── databas_manager.py
|
├── database/
|    ├── courses.json
|    ├── enrollments.json
|    └── students.json
|
├── models
|
├── main.py
└── README.md
```







