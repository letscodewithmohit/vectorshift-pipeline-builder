# VectorShift Pipeline Builder

A React + FastAPI based pipeline builder created as part of the VectorShift Frontend Technical Assessment.

## Features

### Part 1: Node Abstraction

* Created a reusable `BaseNode` component.
* Reduced duplicated code across nodes.
* Added 5 custom nodes:

  * API Node
  * Database Node
  * Email Node
  * Calculator Node
  * Filter Node

### Part 2: Styling

* Added consistent styling across all nodes.
* Improved toolbar layout and responsiveness.
* Enhanced submit and clear actions.
* Added result modal for pipeline analysis.

### Part 3: Text Node Logic

* Dynamic node resizing based on text content.
* Automatic variable detection using `{{variable}}` syntax.
* Dynamic input handles generated from detected variables.

Example:

```text
Hello {{name}}
Email: {{email}}
```

Creates two input handles:

* name
* email

### Part 4: Backend Integration

* Frontend sends pipeline nodes and edges to FastAPI backend.
* Backend calculates:

  * Number of nodes
  * Number of edges
  * Whether the graph is a DAG
* Results are displayed in a user-friendly modal.

## Tech Stack

Frontend:

* React
* React Flow
* Zustand

Backend:

* FastAPI
* Python

## Running the Project

### Frontend

```bash
cd frontend
npm install
npm start
```

### Backend

```bash
cd backend
uvicorn main:app --reload
```

## DAG Validation

The backend performs cycle detection using DFS.

* Acyclic graph → DAG = Yes
* Cyclic graph → DAG = No

## Author

Manmohan Choudhary
