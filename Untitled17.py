{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled17.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPBX0LvDkZYHZlO9qPm44ad",
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
        "<a href=\"https://colab.research.google.com/github/anil-61-omur/c8342-anil-python-covid-19/blob/main/Untitled17.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qPEOHeBcz-Qp",
        "outputId": "592c8391-8786-435e-9f1a-9dc33bb1fafc"
      },
      "source": [
        "age = str.lower(input(\"Are you a cigarette addict older than 75 years old? : \"))\n",
        "if age == \"yes\":\n",
        "    age = True\n",
        "else:\n",
        "    age = False\n",
        "chronic = str.lower(input(\"Do you have a severe chronic disease? : \"))\n",
        "if chronic ==\"yes\":\n",
        "    chronic = True\n",
        "else:\n",
        "    chronic = False\n",
        "immune = str.lower(input(\"Is your immune system too weak? : \"))\n",
        "if immune == \"yes\":\n",
        "    immune = True\n",
        "else:\n",
        "    immune = False\n",
        "risk =  (age) and (chronic) and (immune)\n",
        "\n",
        "if risk == False:\n",
        "    print(\"You are not in risky group\")\n",
        "else:\n",
        "    print(\"You are in risky group\")"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Are you a cigarette addict older than 75 years old? : YES\n",
            "Do you have a severe chronic disease? : YES\n",
            "Is your immune system too weak? : YES\n",
            "You are in risky group\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}