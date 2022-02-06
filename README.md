# Entry task -- blog backend

## Getting started

1. Git
    - Download project
        ```
        git clone https://git.ntu.im/pdogs/pdogs-6/backend-entry-task/entry-task-daphne.git
        ```

2. Setup environment
    - Go to file `entry-task-daphne`
    - Create a new environment
        ```
        conda create --name my-blog python=3.10
        ```
    - Activate environment
        ```
        conda activate my-blog
        ```
    - Install dependencies
        ```
        pip install -r requirements.txt
        ```
    - Copy files
      ```
      cp .env.example .env
      cp docker-compose.yaml.example docker-compose.yaml
      ```

3. Install docker
    - [Docker](https://docs.docker.com/get-docker/)
    - At the same terminal in `step 2` to start the database
        ```
        docker-compose up
        ```

4. Start backend service
    - Install uvicorn
        ```
        pip install uvicorn
        ```
    - Run server
        ```
        uvicorn app:app --reload
        ```
    - Check API in browser http://127.0.0.1:8000/docs


## Database schema

| post    | type      |
|---------|-----------|
| id      | serial    |
| author  | varchar   |
| title   | varchar   |
| content | text      |
| time    | timestamp |

| comment | type      |
|---------|-----------|
| id      | serial    |
| post_id | integer   |
| author  | varchar   |
| content | text      |
| time    | timestamp |

## Classes

#### Post
    id: int
    author: str
    title: str
    content: str
    time: datetime

#### Comment
    id: int
    post_id: int
    author: str
    content: str
    time: datetime

## APIs

#### browse_post : `GET/post` 
    input: none
    output: [Post]

#### read_post : `GET/post/{post_id}`
      input: id
      output: Post

#### add_post : `POST/post`
      input
        - author
        - title
        - content

      output: id

#### edit_post : `PATCH/post/{post_id}`
      input
          - id
          - title
          - content
  
      output: none

#### delete_post : `DELETE/post/{post_id}`
      input: id
      output: none

 #### add_comment : `POST/post/{post_id}/comment`
      input
          - post_id
          - author
          - content
  
      output: id