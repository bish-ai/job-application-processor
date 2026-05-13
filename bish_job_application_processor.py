{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNlyT2Fb+3t7OehHVeeZ0bm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bish-ai/job-application-processor/blob/main/job_application_processor.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OvKk_j_qVjll",
        "outputId": "0610caa8-9a23-4597-ac01-cfcd20642538"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/98.6 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m98.6/98.6 kB\u001b[0m \u001b[31m3.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/548.1 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[91m╸\u001b[0m \u001b[32m542.7/548.1 kB\u001b[0m \u001b[31m26.2 MB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m548.1/548.1 kB\u001b[0m \u001b[31m15.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ],
      "source": [
        "!pip install -q langgraph langchain langchain-openai"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langgraph.graph import StateGraph,START,END\n",
        "from typing import TypedDict\n",
        "#importing all necessariesfrom langgraph.graph import StateGraph, END\n"
      ],
      "metadata": {
        "id": "PuRQRIEOWK24"
      },
      "execution_count": 37,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class JobState(TypedDict):\n",
        "  age: int\n",
        "  name: str\n",
        "  experience: int\n",
        "  skills: list\n",
        "  valid: bool\n",
        "  eligible: bool\n",
        "  score: int\n",
        "  decision: bool\n",
        "  message: str\n",
        "  achievements:str\n",
        "  response: bool\n",
        "  role: str"
      ],
      "metadata": {
        "id": "u5wcWBYyXvlh"
      },
      "execution_count": 71,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "hpRr09cheopc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def age(state:JobState)-> JobState:\n",
        "  # Initialize valid to True or False based on the age condition\n",
        "  state['valid'] = state[\"age\"] >= 18\n",
        "  return state"
      ],
      "metadata": {
        "id": "ZBiM1YCCY7nD"
      },
      "execution_count": 70,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "LeaderRole = \"Leader\"\n",
        "MidRole = \"Mid-level\"\n",
        "JuniorRole = \"Junior\"\n",
        "\n",
        "#defining the experience node\n",
        "def experience_required(state:JobState)-> JobState:\n",
        "  print(f\"Experience node: Initial state['role']: {state.get('role')}\")\n",
        "  if(state[\"experience\"]>=10):\n",
        "    state[\"role\"]=LeaderRole\n",
        "  elif(state[\"experience\"]>=5):\n",
        "    state[\"role\"]=MidRole\n",
        "  else:\n",
        "    state[\"role\"]=JuniorRole\n",
        "  print(f\"Experience node: Final state['role']: {state.get('role')}\")\n",
        "  return state"
      ],
      "metadata": {
        "id": "vUyo-59maRub"
      },
      "execution_count": 69,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "M_RZSrq-brgl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def score_node(state:JobState)->JobState:\n",
        "  print(f\"Score node: Initial state['score']: {state.get('score')}\")\n",
        "  state['score'] = 0 # Initialize score to 0 for fresh calculation\n",
        "\n",
        "  if state[\"experience\"] >= 10 or state[\"achievements\"] == \"ICPC winner\":\n",
        "    state[\"score\"] += 10\n",
        "  elif state[\"experience\"] >= 5 or state[\"achievements\"] == \"National Hackathon Winner\":\n",
        "    state[\"score\"] += 8\n",
        "  elif state[\"experience\"] >= 2 or (\"ai full stack\" in state[\"skills\"]):\n",
        "    state[\"score\"] += 6\n",
        "  else:\n",
        "    state[\"score\"] += 4\n",
        "    print(\"You are not eligible for the job description as mentioned below\")\n",
        "  print(f\"Score node: Final state['score']: {state.get('score')}\")\n",
        "  return state"
      ],
      "metadata": {
        "id": "PmxTKn66bMqT"
      },
      "execution_count": 107,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def decision_node(state:JobState)->JobState:\n",
        "  print(f\"Decision node: Initial state['decision']: {state.get('decision')}, state['message']: {state.get('message')}\")\n",
        "  if state[\"score\"] >= 10:\n",
        "    state[\"decision\"] = True\n",
        "    state[\"message\"] = \"You are eligible for the principle management head role in the company\"\n",
        "    print(state[\"message\"])\n",
        "  elif state[\"score\"] >= 6:\n",
        "    state[\"decision\"] = True\n",
        "    state[\"message\"] = \"You are eligible for the manager role in the company\"\n",
        "    print(state[\"message\"])\n",
        "  else:\n",
        "    state[\"decision\"] = False\n",
        "    state[\"message\"] = \"You are not eligible for the job description as mentioned below\"\n",
        "    print(state[\"message\"])\n",
        "  print(f\"Decision node: Final state['decision']: {state.get('decision')}, state['message']: {state.get('message')}\")\n",
        "  return state"
      ],
      "metadata": {
        "id": "QMn1-ISldGU9"
      },
      "execution_count": 108,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def response_node(state:JobState)->JobState:\n",
        "  print(f\"Response node: Initial state['response']: {state.get('response')}, state['message']: {state.get('message')}\")\n",
        "  if state[\"score\"] >= 10 and state[\"decision\"] is True:\n",
        "    state[\"response\"] = True\n",
        "    state[\"message\"] = \"Your meeting is gonna scheduled soon for the lead role\"\n",
        "    print(state[\"message\"])\n",
        "  elif state[\"score\"] >= 6 and state[\"decision\"] is True:\n",
        "    state[\"response\"] = True\n",
        "    state[\"message\"] = \"Your meeting is gonna scheduled soon for the managerial role\"\n",
        "    print(state[\"message\"])\n",
        "  else:\n",
        "    state[\"response\"] = False\n",
        "    state[\"message\"] = \"You are not eligible\"\n",
        "    print(state[\"message\"])\n",
        "  print(f\"Response node: Final state['response']: {state.get('response')}, state['message']: {state.get('message')}\")\n",
        "  return state"
      ],
      "metadata": {
        "id": "IkmMCL_deqB5"
      },
      "execution_count": 109,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "job_application_processor = StateGraph(JobState)\n",
        "job_application_processor.set_entry_point(\"age_check\")\n",
        "\n",
        "# Add nodes with string identifiers and their corresponding functions\n",
        "job_application_processor.add_node(\"age_check\", age)\n",
        "job_application_processor.add_node(\"experience_categorization\", experience_required)\n",
        "job_application_processor.add_node(\"score_calculation\", score_node)\n",
        "job_application_processor.add_node(\"make_decision\", decision_node)\n",
        "job_application_processor.add_node(\"generate_response\", response_node)\n",
        "\n",
        "# Define the linear flow for initial steps\n",
        "job_application_processor.add_edge(\"age_check\", \"experience_categorization\")\n",
        "job_application_processor.add_edge(\"experience_categorization\", \"score_calculation\")\n",
        "job_application_processor.add_edge(\"score_calculation\", \"make_decision\")\n",
        "\n",
        "# Router function for conditional edges based on the decision\n",
        "def route_decision(state: JobState) -> str:\n",
        "    if state[\"decision\"]:\n",
        "        return \"generate_response\"\n",
        "    else:\n",
        "        return END\n",
        "\n",
        "# Conditional routing after make_decision\n",
        "job_application_processor.add_conditional_edges(\n",
        "    \"make_decision\",\n",
        "    route_decision, # Use the router function\n",
        "    {\n",
        "        \"generate_response\": \"generate_response\", # If route_decision returns \"generate_response\"\n",
        "        END: END # If route_decision returns END\n",
        "    }\n",
        ")\n",
        "\n",
        "# The response node always leads to END\n",
        "job_application_processor.add_edge(\"generate_response\", END)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UXHdiRkaivDG",
        "outputId": "41882182-aafa-49de-9982-565958f3c5d0"
      },
      "execution_count": 113,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<langgraph.graph.state.StateGraph at 0x78a9d0a2a810>"
            ]
          },
          "metadata": {},
          "execution_count": 113
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "workflow=job_application_processor.compile()#compiling the workflow"
      ],
      "metadata": {
        "id": "A-POIwu3j7Sk"
      },
      "execution_count": 114,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "initial_state={\n",
        "    \"age\":18,\n",
        "    \"name\":\"Bishal Mondal\",\n",
        "    \"experience\":6,\n",
        "    \"skills\":[\"ai\"],\n",
        "    \"valid\": False, # Initializing with a default value\n",
        "    \"eligible\": False, # Initializing with a default value\n",
        "    \"score\": 0, # Initializing with a default value\n",
        "    \"decision\": False, # Initializing with a default value\n",
        "    \"message\": \"\", # Initializing with a default value\n",
        "    \"achievements\": \"\", # Initializing with a default value\n",
        "    \"response\": False, # Initializing with a default value\n",
        "    \"role\": \"\" # Initializing with a default value\n",
        "    }"
      ],
      "metadata": {
        "id": "wir7iKWjk3bi"
      },
      "execution_count": 106,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "final_state=workflow.invoke(initial_state)\n",
        "print(final_state)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DDwSg3nTlR0D",
        "outputId": "f8507aaa-1301-45bc-b1d5-db91fe57c5b0"
      },
      "execution_count": 115,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "You are eligible for the manager role in the company\n",
            "Your meeting is gonna scheduled soon for the managerial role\n",
            "{'age': 18, 'name': 'Bishal Mondal', 'experience': 6, 'skills': ['ai'], 'valid': True, 'eligible': False, 'score': 8, 'decision': True, 'message': 'Your meeting is gonna scheduled soon for the managerial role', 'achievements': '', 'response': True, 'role': 'Mid-level'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from IPython.display import Image\n",
        "Image(workflow.get_graph().draw_mermaid_png())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 647
        },
        "id": "64hGEjVhlt_O",
        "outputId": "0be09eac-7072-4b84-f305-83030e840cc1"
      },
      "execution_count": 116,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<IPython.core.display.Image object>"
            ]
          },
          "metadata": {},
          "execution_count": 116
        }
      ]
    }
  ]
}
