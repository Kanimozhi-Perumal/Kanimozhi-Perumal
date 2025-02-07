{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNg5vCIUkmsTViMBOSMXzNK",
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
        "<a href=\"https://colab.research.google.com/github/Kanimozhi-Perumal/Kanimozhi-Perumal/blob/main/task2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Fs71SgsDRzQa"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "To generate images from text prompts using pre-trained generative models like DALL-E-mini or Stable Diffusion, follow these steps:\n",
        "\n",
        "1. Choose a Pre-trained Generative Model\n",
        "DALL-E-mini\n",
        "DALL-E-mini is a smaller version of OpenAI's DALL-E model that can generate images from textual descriptions. It uses a VQ-VAE-2 model for image generation.\n",
        "\n",
        "Stable Diffusion\n",
        "Stable Diffusion is a diffusion-based generative model that can generate high-quality images from a wide range of text prompts. It's known for its ability to generate realistic and diverse images.\n",
        "\n",
        "2. Setting Up the Environment\n",
        "Depending on the model you choose, follow the setup instructions provided in their respective repositories. This usually involves installing dependencies, downloading pre-trained weights, and configuring your environment.\n",
        "\n",
        "3. Generating Images from Text Prompts\n",
        "Once your environment is set up, you can use the model to generate images from text prompts. Here’s a general outline of how you might do this:\n",
        "\n",
        "Using DALL-E-mini\n",
        "python\n",
        "\n",
        "from dalle_mini import DALLEmini\n",
        "\n",
        "# Initialize DALL-E-mini model\n",
        "dalle = DALLEmini()\n",
        "\n",
        "# Example prompt\n",
        "prompt = \"a circle with gradient\"\n",
        "\n",
        "# Generate image\n",
        "image = dalle.generate_image(prompt)\n",
        "\n",
        "# Save or display the generated image\n",
        "image.save(\"generated_image.jpg\")\n",
        "Using Stable Diffusion\n",
        "python\n",
        "import torch\n",
        "from diffuser import Diffuser\n",
        "\n",
        "# Load pre-trained Diffuser model\n",
        "diffuser = Diffuser()\n",
        "\n",
        "# Example prompt\n",
        "prompt = \"a circle with gradient\"\n",
        "\n",
        "# Encode the prompt\n",
        "text = torch.tensor(diffuser.encode_text(prompt))\n",
        "\n",
        "# Generate image\n",
        "with torch.no_grad():\n",
        "    samples = diffuser.generate_images(text)\n",
        "\n",
        "# Save or display the generated image (samples[0])\n",
        "torch.save(samples[0], \"generated_image.pt\")\n",
        "4. Adjusting Parameters and Refining Results\n",
        "Text Prompt: Experiment with different textual descriptions to see how the model interprets and generates images based on variations in the prompt.\n",
        "\n",
        "Model Parameters: Some models allow you to adjust parameters such as temperature (for diversity in outputs), image resolution, and sampling techniques to refine the generated images.\n",
        "\n",
        "5. Evaluating and Using the Generated Images\n",
        "Quality Check: Evaluate the quality of generated images for coherence with the text prompt and overall visual appeal.\n",
        "\n",
        "Application: Use the generated images for various applications such as art creation, concept design, or illustration.\n",
        "\n",
        "6. Considerations\n",
        "Computational Resources: Generating images can be computationally intensive, especially with larger models or higher resolutions. Ensure your system meets the requirements of the chosen model.\n",
        "\n",
        "Model Limitations: Understand the limitations of the model, such as specific styles it can generate well and potential biases in generated outputs.\n",
        "\n",
        "By following these steps, you can effectively utilize pre-trained generative models like DALL-E-mini or Stable Diffusion to create high-quality images from text prompts, tailored to your specific needs.\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "5aTzx-axSRwv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from dalle_mini import DALLEmini\n",
        "\n",
        "# Initialize DALL-E-mini model\n",
        "dalle = DALLEmini()\n",
        "\n",
        "# Example prompt\n",
        "prompt = \"a circle with gradient\"\n",
        "\n",
        "# Generate image\n",
        "image = dalle.generate_image(prompt)\n",
        "\n",
        "# Save or display the generated image\n",
        "image.save(\"generated_image.jpg\")\n",
        "Using Stable Diffusion\n",
        "python\n",
        "import torch\n",
        "from diffuser import Diffuser\n",
        "\n",
        "# Load pre-trained Diffuser model\n",
        "diffuser = Diffuser()\n",
        "\n",
        "# Example prompt\n",
        "prompt = \"a circle with gradient\"\n",
        "\n",
        "# Encode the prompt\n",
        "text = torch.tensor(diffuser.encode_text(prompt))\n",
        "\n",
        "# Generate image\n",
        "with torch.no_grad():\n",
        "    samples = diffuser.generate_images(text)\n",
        "\n",
        "# Save or display the generated image (samples[0])\n",
        "torch.save(samples[0], \"generated_image.pt\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "94RVwmqmSa0I",
        "outputId": "e4edafd3-fe4f-4677-a8e9-a98837a3bd2f"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-2-5b21200cbd2b>, line 14)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-2-5b21200cbd2b>\"\u001b[0;36m, line \u001b[0;32m14\u001b[0m\n\u001b[0;31m    Using Stable Diffusion\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    }
  ]
}