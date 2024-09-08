# Django with Haystack and Elasticsearch

This project demonstrates how to integrate Django with Haystack and Elasticsearch for advanced search functionality. The project includes a basic Django application with a `Post` model and a search feature using Elasticsearch to provide full-text search capabilities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Search Functionality](#search-functionality)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Django Integration**: A basic Django project setup with models and views.
- **Haystack Integration**: Utilizes Haystack to interface with Elasticsearch.
- **Elasticsearch**: Full-text search capabilities with Elasticsearch.
- **Search Form**: Simple search interface to find posts by title or content.

## Installation

### Prerequisites

- Docker
- Docker Compose
- Python 3.10+

### Clone the Repository

```bash
git clone https://github.com/irfa110/django-elasticsearch.git
cd django-elasticsearch

docker-compose up --build   (optional)-> docker-compose up --build -d


### Indexing Data
python manage.py rebuild_index

