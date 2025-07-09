# Multi-Agent YouTube Research & Blog Writer

A simple multi-agent system built with CrewAI that researches YouTube videos and automatically generates blog posts based on video content.

## Overview

This project uses two AI agents working in sequence:

1. **Blog Researcher** - Finds and analyzes YouTube videos on specified topics
2. **Blog Writer** - Creates engaging blog content based on the research

## Features

- 🎥 Search and analyze YouTube channel content
- 🤖 Two specialized AI agents with distinct roles
- 📝 Automatic blog post generation in Markdown format
- 🔄 Sequential workflow with memory and caching
- ⚡ Built on CrewAI framework with GPT-4o-mini

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Tusharbecoding/multi-youtube-agent
   cd multi-youtube-agent
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   Create a `.env` file in the root directory:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Update YouTube channel**
   Edit `tools.py` to specify the target YouTube channel:
   ```python
   yt_tool = YoutubeChannelSearchTool(youtube_channel_handle="@yourchannel")
   ```

## Usage

Run the multi-agent system:

```bash
python crew.py
```

The system will:

1. Research the specified video topic on the configured YouTube channel
2. Generate a comprehensive blog post
3. Save the output to `blog_post.md`

## Project Structure

```
multi-youtube-agent/
├── agents.py      # AI agent definitions (researcher & writer)
├── tasks.py       # Task definitions for each agent
├── tools.py       # YouTube search tool configuration
├── crew.py        # Main orchestration and execution
└── requirements.txt
```

## Customization

- **Change the topic**: Modify the `topic` parameter in `crew.py`
- **Adjust agent behavior**: Edit agent backstories and goals in `agents.py`
- **Modify output format**: Update task descriptions in `tasks.py`
- **Switch YouTube channel**: Update the channel handle in `tools.py`

## Dependencies

- `crewai` - Multi-agent framework
- `crewai-tools` - YouTube integration tools
- `python-dotenv` - Environment variable management
- `openai` - GPT model access

## Output

The system generates a `blog_post.md` file containing a well-structured blog post based on the YouTube video research.
