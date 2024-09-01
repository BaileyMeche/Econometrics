{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPpV/jkg92G3RQZ6zYyrxTl",
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
        "<a href=\"https://colab.research.google.com/github/BaileyMeche/Econometrics/blob/main/DifferenceinDifferences.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Difference-in-Differences"
      ],
      "metadata": {
        "id": "NRxZSc-y0Gm3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install causaldata"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-NAJT_08yK3i",
        "outputId": "fbea19e0-e251-469b-a1c8-14561bc00ce2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: causaldata in /usr/local/lib/python3.10/dist-packages (0.1.3)\n",
            "Requirement already satisfied: statsmodels in /usr/local/lib/python3.10/dist-packages (from causaldata) (0.14.0)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (from causaldata) (1.5.3)\n",
            "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas->causaldata) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas->causaldata) (2023.3.post1)\n",
            "Requirement already satisfied: numpy>=1.21.0 in /usr/local/lib/python3.10/dist-packages (from pandas->causaldata) (1.23.5)\n",
            "Requirement already satisfied: scipy!=1.9.2,>=1.4 in /usr/local/lib/python3.10/dist-packages (from statsmodels->causaldata) (1.11.3)\n",
            "Requirement already satisfied: patsy>=0.5.2 in /usr/local/lib/python3.10/dist-packages (from statsmodels->causaldata) (0.5.3)\n",
            "Requirement already satisfied: packaging>=21.3 in /usr/local/lib/python3.10/dist-packages (from statsmodels->causaldata) (23.2)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from patsy>=0.5.2->statsmodels->causaldata) (1.16.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install linearmodels"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cbCRSImTz4LQ",
        "outputId": "02301cc5-ab7c-4228-8838-94b907c0e225"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: linearmodels in /usr/local/lib/python3.10/dist-packages (5.3)\n",
            "Requirement already satisfied: numpy>=1.19.0 in /usr/local/lib/python3.10/dist-packages (from linearmodels) (1.23.5)\n",
            "Requirement already satisfied: pandas>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from linearmodels) (1.5.3)\n",
            "Requirement already satisfied: scipy>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from linearmodels) (1.11.3)\n",
            "Requirement already satisfied: statsmodels>=0.12.0 in /usr/local/lib/python3.10/dist-packages (from linearmodels) (0.14.0)\n",
            "Requirement already satisfied: mypy-extensions>=0.4 in /usr/local/lib/python3.10/dist-packages (from linearmodels) (1.0.0)\n",
            "Requirement already satisfied: Cython>=0.29.34 in /usr/local/lib/python3.10/dist-packages (from linearmodels) (3.0.4)\n",
            "Requirement already satisfied: pyhdfe>=0.1 in /usr/local/lib/python3.10/dist-packages (from linearmodels) (0.2.0)\n",
            "Requirement already satisfied: formulaic>=0.6.5 in /usr/local/lib/python3.10/dist-packages (from linearmodels) (0.6.6)\n",
            "Requirement already satisfied: setuptools-scm[toml]<8.0.0,>=7.0.0 in /usr/local/lib/python3.10/dist-packages (from linearmodels) (7.1.0)\n",
            "Requirement already satisfied: astor>=0.8 in /usr/local/lib/python3.10/dist-packages (from formulaic>=0.6.5->linearmodels) (0.8.1)\n",
            "Requirement already satisfied: interface-meta>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from formulaic>=0.6.5->linearmodels) (1.3.0)\n",
            "Requirement already satisfied: typing-extensions>=4.2.0 in /usr/local/lib/python3.10/dist-packages (from formulaic>=0.6.5->linearmodels) (4.5.0)\n",
            "Requirement already satisfied: wrapt>=1.0 in /usr/local/lib/python3.10/dist-packages (from formulaic>=0.6.5->linearmodels) (1.14.1)\n",
            "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.0->linearmodels) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.0->linearmodels) (2023.3.post1)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from setuptools-scm[toml]<8.0.0,>=7.0.0->linearmodels) (23.2)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from setuptools-scm[toml]<8.0.0,>=7.0.0->linearmodels) (67.7.2)\n",
            "Requirement already satisfied: tomli>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from setuptools-scm[toml]<8.0.0,>=7.0.0->linearmodels) (2.0.1)\n",
            "Requirement already satisfied: patsy>=0.5.2 in /usr/local/lib/python3.10/dist-packages (from statsmodels>=0.12.0->linearmodels) (0.5.3)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from patsy>=0.5.2->statsmodels>=0.12.0->linearmodels) (1.16.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Two-way fixed effects"
      ],
      "metadata": {
        "id": "DQZz9nXZtx5z"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Kessler and Roth organ donation study discussed earlier with clustered fixed effects applied at the state level"
      ],
      "metadata": {
        "id": "75yZ2RQSDPlk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import linearmodels as lm\n",
        "from causaldata import organ_donations"
      ],
      "metadata": {
        "id": "YDyG_imyD9a7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create the variable columns we need"
      ],
      "metadata": {
        "id": "3c90Pt37HnCc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "od = organ_donations.load_pandas().data\n",
        "\n",
        "# Create Treatment Variable\n",
        "od['California'] = od['State'] == 'California'\n",
        "od['After'] = od['Quarter_Num'] > 3\n",
        "od['Treated'] = 1*(od['California'] & od['After'])\n",
        "# Set our individual and time (index) for our data\n",
        "od = od.set_index(['State','Quarter_Num'])"
      ],
      "metadata": {
        "id": "rrtZvjvJHdMx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Visualizing the data:\n",
        "od"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 455
        },
        "id": "DB4D0wEcHp4P",
        "outputId": "34276300-839a-49dd-d1f5-de5eea54a230"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                    Quarter    Rate  California  After  Treated\n",
              "State   Quarter_Num                                            \n",
              "Alaska  1            Q42010  0.7500       False  False        0\n",
              "        2            Q12011  0.7700       False  False        0\n",
              "        3            Q22011  0.7700       False  False        0\n",
              "        4            Q32011  0.7800       False   True        0\n",
              "        5            Q42011  0.7800       False   True        0\n",
              "...                     ...     ...         ...    ...      ...\n",
              "Wyoming 2            Q12011  0.5946       False  False        0\n",
              "        3            Q22011  0.5937       False  False        0\n",
              "        4            Q32011  0.5911       False   True        0\n",
              "        5            Q42011  0.5854       False   True        0\n",
              "        6            Q12012  0.5881       False   True        0\n",
              "\n",
              "[162 rows x 5 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-d733d74e-5880-439d-9799-fb3840d10f3c\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>Quarter</th>\n",
              "      <th>Rate</th>\n",
              "      <th>California</th>\n",
              "      <th>After</th>\n",
              "      <th>Treated</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>State</th>\n",
              "      <th>Quarter_Num</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"5\" valign=\"top\">Alaska</th>\n",
              "      <th>1</th>\n",
              "      <td>Q42010</td>\n",
              "      <td>0.7500</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Q12011</td>\n",
              "      <td>0.7700</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Q22011</td>\n",
              "      <td>0.7700</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Q32011</td>\n",
              "      <td>0.7800</td>\n",
              "      <td>False</td>\n",
              "      <td>True</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Q42011</td>\n",
              "      <td>0.7800</td>\n",
              "      <td>False</td>\n",
              "      <td>True</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th rowspan=\"5\" valign=\"top\">Wyoming</th>\n",
              "      <th>2</th>\n",
              "      <td>Q12011</td>\n",
              "      <td>0.5946</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Q22011</td>\n",
              "      <td>0.5937</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Q32011</td>\n",
              "      <td>0.5911</td>\n",
              "      <td>False</td>\n",
              "      <td>True</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Q42011</td>\n",
              "      <td>0.5854</td>\n",
              "      <td>False</td>\n",
              "      <td>True</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Q12012</td>\n",
              "      <td>0.5881</td>\n",
              "      <td>False</td>\n",
              "      <td>True</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>162 rows × 5 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-d733d74e-5880-439d-9799-fb3840d10f3c')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-d733d74e-5880-439d-9799-fb3840d10f3c button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-d733d74e-5880-439d-9799-fb3840d10f3c');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-ae59464d-60a5-48a6-9783-4dba531804ca\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-ae59464d-60a5-48a6-9783-4dba531804ca')\"\n",
              "            title=\"Suggest charts.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-ae59464d-60a5-48a6-9783-4dba531804ca button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "\n",
        "mod = lm.PanelOLS.from_formula('''Rate ~\n",
        "Treated + EntityEffects + TimeEffects''',od)\n",
        "\n",
        "# Specify clustering when we fit the model\n",
        "clfe = mod.fit(cov_type = 'clustered',\n",
        "cluster_entity = True)\n",
        "print(clfe)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sMyI0nm20MDm",
        "outputId": "d7b85083-255b-46ce-eeac-3633623e4b09"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                          PanelOLS Estimation Summary                           \n",
            "================================================================================\n",
            "Dep. Variable:                   Rate   R-squared:                        0.0092\n",
            "Estimator:                   PanelOLS   R-squared (Between):             -0.0010\n",
            "No. Observations:                 162   R-squared (Within):              -0.0021\n",
            "Date:                Thu, Nov 02 2023   R-squared (Overall):             -0.0010\n",
            "Time:                        03:36:08   Log-likelihood                    388.57\n",
            "Cov. Estimator:             Clustered                                           \n",
            "                                        F-statistic:                      1.2006\n",
            "Entities:                          27   P-value                           0.2752\n",
            "Avg Obs:                       6.0000   Distribution:                   F(1,129)\n",
            "Min Obs:                       6.0000                                           \n",
            "Max Obs:                       6.0000   F-statistic (robust):             11.525\n",
            "                                        P-value                           0.0009\n",
            "Time periods:                       6   Distribution:                   F(1,129)\n",
            "Avg Obs:                       27.000                                           \n",
            "Min Obs:                       27.000                                           \n",
            "Max Obs:                       27.000                                           \n",
            "                                                                                \n",
            "                             Parameter Estimates                              \n",
            "==============================================================================\n",
            "            Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI\n",
            "------------------------------------------------------------------------------\n",
            "Treated       -0.0225     0.0066    -3.3949     0.0009     -0.0355     -0.0094\n",
            "==============================================================================\n",
            "\n",
            "F-test for Poolability: 191.71\n",
            "P-value: 0.0000\n",
            "Distribution: F(31,129)\n",
            "\n",
            "Included effects: Entity, Time\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "clfe.params"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KSza7spiK3U_",
        "outputId": "dfb058c5-b250-4313-d6ab-c5a053e266f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Treated   -0.022459\n",
              "Name: parameter, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "  plt.figure(figsize=(10, 6))\n",
        "  sns.scatterplot(x='Quarter_Num', y='Rate', data=od, label='Data', color='blue', alpha=0.5)\n",
        "  plt.axvline(x=3, color='red', linestyle='--', label='Treatment Time')\n",
        "  plt.xlabel('Quarter')\n",
        "  plt.ylabel('Rate')\n",
        "  plt.legend()\n",
        "  plt.title('Regression Analysis with Treatment Time')\n",
        "  plt.grid()\n",
        "  plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 497
        },
        "id": "aCefDPKJKKc3",
        "outputId": "6505e54f-671f-45d9-cf85-de49d62021b7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "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h549e2L06NEAgIKCAnzwwQe46667MHPmTBgMBnz44YcYNWoUDhw4gNjYWKtxDB06FBEREVizZo357ylbs2YNOnbsiH79+gEA/v73v+PYsWN47LHHoNfrcfHiRSQnJyMjI6PWcSbvv/8+Hn/8cUyaNAlPPPEESkpK8Ntvv+Gnn37C3XffbfU1KpUKAwYMwO7du81lv/32G65cuQI3Nzfs3bsXt912GwDghx9+wA033GDurlXd6tWra3Tv6tixo8VzJk+ejKioKCQlJeHw4cP44IMPEBISYq5f12Lnzp34/PPPMXv2bAQFBUGv1yM7Oxt/+9vfzIlVcHAwtm7divvvvx8FBQV48sknATTsbxocHIx3330XjzzyCG6//XZMnDgRAHD99debY6ioqMDo0aMxePBgvPbaa1izZg1mz54NHx8fvPDCC7jnnnswceJELFu2DNOmTUO/fv0QFRUFAA3+v5R9+umnMBgMeOihh6BSqfDaa69h4sSJOHv2LDQaDR566CFkZmYiOTm5Rje85jJlyhRER0dj0aJF2Lx5M1555RUEBgZi+fLlGDZsGF599VWsWbMGc+bMwU033YTBgwcDEMn6+PHjsWfPHjz44IOIjo7G0aNH8dZbb+HkyZNNOm6OiK6RRETUDFauXCkBkL799lspJydHOnfunLRu3TopODhY0mq10rlz58zPHT58uNSzZ0+ppKTEXGYymaT+/ftLnTp1Mpc99thjkkqlkn755Rdz2aVLl6TAwEAJgJSammouj4yMlABI27Zts4jr5Zdflnx8fKSTJ09alD///POSWq2WMjIyJEmSpCeeeELy8/OTysvLa/2MMTEx0m233Vbn72HevHlS1UPtkSNHJADSAw88YPG8OXPmSACknTt31vgMu3fvNpddvHhR0mq10tNPP13n+8p69uwp3XPPPebtf/zjH1JQUJBkNBotnjdkyBAJgPTxxx+by0pLS6WwsDDp73//u7msvLxcKi0ttXjt5cuXpdDQUOm+++6zKAcgzZs3z7ydmJgoabVaKT8/3+LzuLu7m593+fJlCYD073//u87PNWTIEGnIkCHm7QkTJkjdu3ev8zXW/Pvf/5bUarVUUFAgSZIkvf3221JkZKTUp08f6bnnnpMkSZIqKiokf39/6amnnjK/rvrfVZIkycfHR5o+fXqN95CfW/33c/vtt0utW7e2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H34Y3333HQYMGICKigocP34cn3/+uXktOiJyAEpM5UdErk+ejvznn3+usa+iokLq2LGj1LFjR/N032fOnJGmTZsmhYWFSRqNRmrbtq00duxYad26dRav/eWXX6RBgwZJWq1WateunZSUlCS9/fbbEgApKyvL/LzIyMhapwo3GAxSYmKidN1110keHh5SUFCQ1L9/f+n111+XysrKJEmSpHXr1km33HKLFBISInl4eEjt27eXHnroIenChQvmn/PKK69Iffr0kfz9/SUvLy+pa9eu0r/+9S/zz5Ak69NWG41GacGCBVJUVJSk0WikiIgIKTEx0WI69ro+Q/WpuKv78ssvJQDShx9+WOtzdu3aJQGQlixZYv6Z1qbznj59uhQZGWneNplM0sKFC6XIyEhJq9VKN9xwg7Rp06Yaz5OkmtM2y0pLS6WAgACpVatW0tWrVy325ebmSrNmzZK6du0q+fj4SK1atZL69u0rff7553X+DpYvXy4NHjxYat26taTVaqWOHTtKzzzzjHTlypVafwdV3XTTTRIA6aeffjKX/fnnnxIAKSIiosbzrf1djx8/Lg0ePFjy8vKSAJinnJafm5OTY/F8+X+k6jT69altOvJZs2ZZfX52drY0a9YsKSIiQtJoNFJYWJg0fPhw6b333jM/x5a/6b59+6RevXpJHh4eFn/f6dOnSz4+PjXev7Z6Za1uN+T/Up6O3Np09dXrW3l5ufTYY49JwcHBkkqlsmlq8sZMR17972vL76SsrEx69dVXpe7du0tarVYKCAiQevXqJS1YsKDBdZiImp9KkhQcSUlE1ASefPJJLF++HIWFhbUOxibHUV5ejvDwcIwbNw4ffvih0uEQERE1CMc4EZFTuXr1qsX2pUuXsHr1agwcOJBJk5PYsGEDcnJyMG3aNKVDISIiajC2OBGRU4mNjcXQoUMRHR2N7OxsfPjhh8jMzMSOHTswePBgpcOjOvz000/47bff8PLLLyMoKMjmxVWJiIiUxMkhiMipjBkzBuvWrcN7770HlUqFG2+8ER9++CGTJifw7rvv4pNPPkFsbCxWrVqldDhEREQ2YYsTERERERFRPTjGiYiIiIiIqB5MnIiIiIiIiOrR4sY4mUwmZGZmQqfTNWixTCIiIiIick2SJMFgMCA8PBxubnW3KbW4xCkzMxMRERFKh0FERERERA7i3LlzaNeuXZ3PaXGJk06nAyB+OX5+fgpHAxiNRnzzzTe45ZZboNFolA6HHBzrC9nEaETFhx8iJSUFXZKSoPH2VjoicgI8zpCtWGfIVo5UZwoKChAREWHOEerS4hInuXuen5+fwyRO3t7e8PPzU7zikONjfSGbFBUBzz2H/gCMb70FjQMc88jx8ThDtmKdIVs5Yp1pyBAeTg5BRERERERUDyZORERERERE9WDiREREREREVI8WN8aJiIiIiJQjSRLKy8tRUVGhdCikEKPRCHd3d5SUlNilHmg0GqjV6mv+OUyciIiIiMguysrKcOHCBRQXFysdCilIkiSEhYXh3LlzdllXVaVSoV27dvD19b2mn8PEiYiIiIianclkQmpqKtRqNcLDw+Hh4WGXi2ZyPCaTCYWFhfD19a130dlrJUkScnJy8Oeff6JTp07X1PLExImIyFVptSjfsAEHDx5EL61W6WiIqIUrKyuDyWRCREQEvLmuXItmMplQVlYGT0/PZk+cACA4OBhpaWkwGo1MnIiIyAp3d0hjxiD7r++JiByBPS6UiapqqpZNxWvu0qVLodfr4enpib59++LAgQN1Pn/x4sXo0qULvLy8EBERgaeeegolJSV2ipaIiIiIiFoiRROntWvXIiEhAfPmzcPhw4cRExODUaNG4eLFi1af/+mnn+L555/HvHnzkJKSgg8//BBr167FP/7xDztHTkTkBIxGqD7+GBE7dgBGo9LREBEROTVF+268+eabmDlzJuLj4wEAy5Ytw+bNm7FixQo8//zzNZ6/b98+DBgwAHfffTcAQK/X46677sJPP/1U63uUlpaitLTUvF1QUABATINodIALCTkGR4iFHB/rC9mkqAiaBx7AjQCKX3wR0GiUjoicAI8zZKuG1hmj0QhJkmAymWAymewRGjkoSZLMj/aoCyaTCZIkWR3jZMuxTrHEqaysDIcOHUJiYqK5zM3NDSNGjMD+/futvqZ///745JNPcODAAfTp0wdnz57Fli1bMHXq1FrfJykpCQsWLKhR/s033zjUwMTk5GSlQyAnwvpCDaEuKcHYv77fuXMnKjw9FY2HnAuPM2Sr+uqMu7s7wsLCUFhYiLKyMjtF1TQeffRR/O9//wMgPkdAQAC6d++Ov//977j77rsbPG7r008/RWJiItLT05szXKdhMBjs8j5lZWW4evUqdu/ejfLy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mDdvHhYvXoz27dvjvvvuw9133w2dToclS5bA29sbkydPxty5c/Huu+8CANasWYO5c+finXfewQ033IBffvkFM2fOhI+PD6ZPn27+HC+88AJef/11dOrUCS+88ALuuusunD59Gv3798fixYstWtt8m3DA7JkzZ7B161Zs27YNZ86cwaRJk3D27Fl07twZ33//Pfbt24f77rsPI0aMQN++fQEAd9xxB7y8vLB161a0atUKy5cvx/Dhw3Hy5MlmG0PFxImIiIiI6Bq89NJLGDlyJACgtLQUCxcuxLfffot+/foBADp06IA9e/Zg+fLlGDJkCDQaDRYsWGB+fVRUFPbv34/PP/8ckydPhq+vL7y8vFBaWoqwsLAa7zdnzhyMGjUKAPDEE0/grrvuwo4dOzBgwAAAwP33349Vq1aZnz9v3jy88cYbmDhxovn9/vjjDyxfvtwicZozZw5uu+02AMCCBQvQvXt3nD59Gl27drVobWtqJpMJK1asgE6nQ7du3XDzzTfjxIkT2LJlC9zc3NClSxe8+uqr+O6779C3b1/s2bMHBw4cwMWLF6HVagEAr7/+OjZs2IB169bhwQcfbPIYASZORERERKS0utZJUKstty9erP25btVGoaSlNTokW/Tu3dv8/enTp1FcXGxOpGRlZWW44YYbzNtLly7FihUrkJGRgatXr6KsrAyxsbENer/rr7/e/H1oaCgAoGfPnhZlF//6PRUVFeHMmTO4//77MXPmTPNzysvL0apVq1p/bps2bQAAFy9eRNeuXRsUV2Pp9XroqnSTCA0NhVqthluVv2fVz/Trr7+isLAQrVu3tvg5V69exZkzZ5otTiZORERERKQsHx/ln3sNfKq8T+FfSeDmzZvRtm1bi+fJrSOfffYZ5syZgzfeeAP9+vWDTqfDv//9b/z0008Nej9Nlf76KpXKapnJZLKI5/333zd3c5OpqyWl1n6u/HOak6ba+AOVSmW1rOpnatOmDXZV7Zb5l/pm/rsWTJwUZDCI8SoAkJICREVxtisiakIeHqhYsgTHjh1DtIeH0tEQEbUI3bp1g1arRUZGBoYMGWL1OXv37kX//v3x6KOPmsuqt5R4eHigoqLimuMJDQ1FeHg4zp49i3vuuafRP6ep4mkKN954I7KysuDu7g69Xm+392XipJC0tMrppWNigA0bAH9/MYWwHf/+ROTK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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Table 18.2 shows the result of this two-way fixed effects regression, with the fixed effects themselves excluded from the table and only the coefficient on the `Treated`\n",
        " variable (“treated-group” and “after-treatment” interacted) shown. Notice at the bottom of the table a row each for the state and quarter fixed effects. The “X” here just indicates that the fixed effects are included. It’s fairly common to skip reporting the actual fixed effects - there are so many of them!\n",
        "\n",
        "The coefficient is **-0.022** with a standard error of .006. From this we can say that the introduction of active-choice phrasing in California saw a reduction in organ donation rates that was .022 (or 2.2 percentage points) larger in California than it was in the untreated states. The standard error is .006, so we have a t-statistic of **-0.22/0.006 = 3.67**, which is high enough to be considered statistically significant at the 99% level. We can reject the null that the DID estimate is 0."
      ],
      "metadata": {
        "id": "DRlq8KcdDUqN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Supporting the Parallel Trends Assumption\n"
      ],
      "metadata": {
        "id": "iWUTsf0DuIhl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import linearmodels as lm\n",
        "from causaldata import organ_donations\n",
        "od = organ_donations.load_pandas().data\n",
        "\n",
        "# Keep only pre-treatment data\n",
        "od = od.loc[od['Quarter_Num'] <= 3]\n",
        "\n",
        "# Create fake treatment variables\n",
        "od['California'] = od['State'] == 'California'\n",
        "od['FakeAfter1'] = od['Quarter_Num'] > 1\n",
        "od['FakeAfter2'] = od['Quarter_Num'] > 2\n",
        "od['FakeTreat1'] = 1*(od['California'] & od['FakeAfter1'])\n",
        "od['FakeTreat2'] = 1*(od['California'] & od['FakeAfter2'])\n",
        "\n",
        "# Set our individual and time (index) for our data\n",
        "od = od.set_index(['State','Quarter_Num'])\n",
        "\n",
        "# Run the same model as before\n",
        "# but with our fake treatment variables\n",
        "mod1 = lm.PanelOLS.from_formula('''Rate ~\n",
        "FakeTreat1 + EntityEffects + TimeEffects''',od)\n",
        "mod2 = lm.PanelOLS.from_formula('''Rate ~\n",
        "FakeTreat2 + EntityEffects + TimeEffects''',od)\n",
        "\n",
        "clfe1 = mod1.fit(cov_type = 'clustered',\n",
        "cluster_entity = True)\n",
        "clfe2 = mod1.fit(cov_type = 'clustered',\n",
        "cluster_entity = True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7oEwNqG71Tu1",
        "outputId": "fbdec4be-7b5e-47a6-bde9-c6ce55c1ad2a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-7-d7ce3cab5625>:9: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  od['California'] = od['State'] == 'California'\n",
            "<ipython-input-7-d7ce3cab5625>:10: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  od['FakeAfter1'] = od['Quarter_Num'] > 1\n",
            "<ipython-input-7-d7ce3cab5625>:11: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  od['FakeAfter2'] = od['Quarter_Num'] > 2\n",
            "<ipython-input-7-d7ce3cab5625>:12: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  od['FakeTreat1'] = 1*(od['California'] & od['FakeAfter1'])\n",
            "<ipython-input-7-d7ce3cab5625>:13: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  od['FakeTreat2'] = 1*(od['California'] & od['FakeAfter2'])\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import linearmodels as lm\n",
        "from causaldata import organ_donations\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "# Load the data\n",
        "od = organ_donations.load_pandas().data\n",
        "\n",
        "# Keep only pre-treatment data\n",
        "od = od.loc[od['Quarter_Num'] <= 3]\n",
        "\n",
        "# Create fake treatment variables\n",
        "od['California'] = od['State'] == 'California'\n",
        "od['FakeAfter1'] = od['Quarter_Num'] > 1\n",
        "od['FakeAfter2'] = od['Quarter_Num'] > 2\n",
        "od['FakeTreat1'] = 1 * (od['California'] & od['FakeAfter1'])\n",
        "od['FakeTreat2'] = 1 * (od['California'] & od['FakeAfter2'])\n",
        "\n",
        "# Set our individual and time (index) for our data\n",
        "od = od.set_index(['State', 'Quarter_Num'])\n",
        "\n",
        "# Create two separate dataframes for treated=0 and treated=1\n",
        "od_treated_0 = od[od['FakeTreat1'] == 0]\n",
        "od_treated_1 = od[od['FakeTreat1'] == 1]\n",
        "\n",
        "# Create two plots with different treatment dates\n",
        "fig, axes = plt.subplots(2, 1, figsize=(8, 10))\n",
        "\n",
        "# Plot for FakeTreat1\n",
        "sns.scatterplot(x='Quarter_Num', y='Rate', data=od_treated_0.reset_index(), label='Treated=0', ax=axes[0], alpha=0.5)\n",
        "sns.scatterplot(x='Quarter_Num', y='Rate', data=od_treated_1.reset_index(), label='Treated=1', ax=axes[0], alpha=0.5)\n",
        "axes[0].axvline(x=2, color='red', linestyle='--', label='Treatment Date 1')\n",
        "axes[0].set_xlabel('Quarter')\n",
        "axes[0].set_ylabel('Rate')\n",
        "axes[0].legend()\n",
        "axes[0].set_title('Data Visualization for FakeTreat1')\n",
        "\n",
        "# Plot for FakeTreat2\n",
        "sns.scatterplot(x='Quarter_Num', y='Rate', data=od_treated_0.reset_index(), label='Treated=0', ax=axes[1], alpha=0.5)\n",
        "sns.scatterplot(x='Quarter_Num', y='Rate', data=od_treated_1.reset_index(), label='Treated=1', ax=axes[1], alpha=0.5)\n",
        "axes[1].axvline(x=3, color='red', linestyle='--', label='Treatment Date 2')\n",
        "axes[1].set_xlabel('Quarter')\n",
        "axes[1].set_ylabel('Rate')\n",
        "axes[1].legend()\n",
        "axes[1].set_title('Data Visualization for FakeTreat2')\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "WSLZwKSLR7WI",
        "outputId": "fd0abf95-6e70-4e9f-d293-1de42e5d7937"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-8-4b8d6877de42>:13: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  od['California'] = od['State'] == 'California'\n",
            "<ipython-input-8-4b8d6877de42>:14: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  od['FakeAfter1'] = od['Quarter_Num'] > 1\n",
            "<ipython-input-8-4b8d6877de42>:15: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  od['FakeAfter2'] = od['Quarter_Num'] > 2\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x1000 with 2 Axes>"
            ],
            "image/png": "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Li7GM888g/DwcPj6+iI0NBTx8fEA0GBSYLN9+3akpKTY69SHhoba2zk0Zh2jR4+GXq/Ht99+C6CmF6SzZ8/aG23XZdSoURg0aBAee+wxhIeH48EHH8TatWubnWRkZ2fbL4o1Gg1CQ0PtbQkauy+ulpOTY49z0aJFDvNaY99f7dy5c+jWrVut8h49etjnX6ljx44O74OCggCgSW0JrvxuAHV+f1FRkT15tLFtb2P17NkTKSkpDpNKpYLVasWbb76Jrl27QqlUIiQkBKGhofjzzz+d7stnn30We/bswebNm3Httdc6zDt58iTKysoQFhaG0NBQh0mn09kbrjfW1dt46tQpCIKAV155pdb6Z8+eDeBy4/imbhcRtV9sY0FEbiUnJwdlZWXo0qWLvWzkyJHYsWMHnn/+efTp0wcajQZWqxW33357oy7QT58+jVtvvRXdu3fHokWLEBsbC4VCgR9++AFvvvlmo9Zhazj7+eef4+GHH8bnn38OHx+fBscn8PX1xbZt27B161Z8//332LBhA9asWYNbbrkFP/30E3x8fOocUM9isdR6P3ToUBQXF+Nf//oXunfvDj8/P+Tm5mL8+PHNSlZMJhMeeOABKJVKrF27tlaPVi3d963Bx8fHabnQiPYOraG1eiebP38+XnnlFTz66KN49dVXERwcDKlUimeffdbpvhwxYgRWr16NBQsW4OOPP3bostdqtSIsLAyfffaZ0++qq31LXa7eRls806dPx7Bhw5x+xvZ/tKnbRUTtFxMLInIrtgbFtouZkpISZGRkYO7cuQ6NpE+ePFnrs3VdoP/f//0fqqqq8N133znc/W5KdRGlUokHHngAH3/8MQoKCrBu3TrccsstiIiIaPCzUqkUt956K2699VYsWrQI8+fPx0svvYStW7ciJSXFfgf+6sHlrr5zf/DgQZw4cQIfffQRxo4day/ftGlTo7fjak8//TQOHDiAbdu22Rs327TGvnemU6dOOH78eK3yY8eO2ee3Fdu66/r+kJCQBruTba7169fj73//Oz788EOH8tLSUnuD9yvde++9uO222zB+/Hj4+/s79GLWuXNnbN68GYMGDWqTbplt3dTK5XKkpKTUu2xjt8sdRqQnorbFqlBE5Da2bNmCV199FfHx8fYqRra71VffnV68eHGtz9suCK++QHe2jrKyMqxcubJJ8Y0ePRrV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ZkyZMgXPPvssQkJCMGzYsDbbT0RE3oqJBRERNai4uBgbN27EU089BV9fX4d5ERERGD16NNasWQNBEBq1Pn9/f6xatQpHjhzBkiVL8P777+PNN990WObUqVP48ssv8dVXX+HAgQNYsmQJBgwYgIkTJyIvLw95eXmIjY1FaWkpbrnlFvTt2xe///47NmzYgIKCAowcOdJhfR999BEUCgW2b9+O5cuXt2yHEBFRLTKxAyAiIvd38uRJCIKAHj16OJ3fo0cPlJSU4OLFi41a38svv2x/HRcXh+nTp2P16tV44YUX7OUmkwkff/wxQkND7WUKhQJqtRoRERH2sqVLl6Jv376YP3++vWzFihWIjY3FiRMncM011wAAunbtitdee61xG0xERE3GxIKIiBqtoScSCoWiUetZs2YN3nrrLZw+fRo6nQ5msxkBAQEOy3Tq1MkhqajLH3/8ga1bt0Kj0dSad/r0aXtikZSU1KjYiIioeVgVioiIGtSlSxdIJBIcPXrU6fyjR48iNDQUWq0WEomkVgJyZfuJnTt3YvTo0bjjjjvwv//9D/v378dLL71Uq0G1n59fo2LT6XS4++67ceDAAYfp5MmTuOmmm5q8PiIiah4+sSAiogZ16NABQ4cOxX//+19MnTrVoZ1Ffn4+PvvsM0yePBkAEBoairy8PPv8kydPwmAw2N/v2LEDnTp1sjf2BoBz5841Kg6FQgGLxeJQdv311+PLL79EXFwcZDL+rBERiYVPLIiIqFGWLl2KqqoqDBs2DNu2bcP58+exYcMGDB06FNdccw1mzZoFALjllluwdOlS7N+/H7///jueeOIJyOVy+3q6du2K7OxsrF69GqdPn8Zbb72Fr7/+ulExxMXFYdeuXTh79iyKiopgtVoxefJkFBcX46GHHsKePXtw+vRpbNy4EWlpabWSECIiajtMLIiIqFG6du2KPXv2ICEhASNHjkSnTp0wfPhwXHPNNdi+fbu9jcMbb7yB2NhYDB48GA8//DCmT58OtVptX88999yDqVOnYsqUKejTpw927NiBV155pVExTJ8+HT4+PkhMTERoaCiys7MRFRWF7du3w2Kx4LbbbkPPnj3x7LPPQqvVQirlzxwRkatIhMb2DUhERHSV2bNnY9GiRdi0aRP+9re/iR0OERGJiIkFERG1yMqVK1FWVoann36aTwiIiLwYEwsiIiIiImox3loiIiIiIqIWY2JBREREREQtxsSCiIiIiIhajIkFERERERG1GBMLIiIiIiJqMSYWRERERETUYkwsiIiIiIioxZhYEBERERFRizGxICIiIiKiFmNiQURERERELcbEgoiIiIiIWoyJBRERERERtRgTCyIiIiIiajEmFkRERERE1GJMLIiIWtGcOXMgkUjEDsNpHHFxcRg/frzLYxHrewFgz549GDhwIPz8/CCRSHDgwAFR4miKzMxMSCQSrF+/XuxQiIiahIkFEbnUqlWrIJFI7JNKpUJUVBSGDRuGt956CxUVFc1e944dOzBnzhyUlpa2Wry9evVCx44dIQhCncsMGjQI4eHhMJvNrfa9nqYt9n1LVVdXIzU1FcXFxXjzzTfxySefoFOnTm32fbaEwNn04IMPttn31uXq/2t1TXFxcS6J58KFC5gzZ47T5O6rr77CqFGjkJCQALVajW7duuG5555zq+OJiBomEzsAIvJO8+bNQ3x8PKqrq5Gfn4/MzEw8++yzWLRoEb777jv06tWryevcsWMH5s6di/Hjx0Or1bZKnKNHj8aMGTPwyy+/4Kabbqo1/+zZs9i5cyemTJkCmUyGl19+GTNmzGiV725tx48fh1TaNveT6tv3bfm99Tl9+jTOnTuH999/H4899pjLvvfpp5/GDTfc4FDmqov3K91000345JNPHMoee+wx9O/fH5MmTbKXaTQal8Rz4cIFzJ07F3FxcejTp4/DvEmTJiEqKgqPPPIIOnbsiIMHD2Lp0qX44YcfsG/fPvj6+rokRiJqGSYWRCSK4cOHo1+/fvb3M2fOxJYtW3DXXXfhnnvuwdGjR93iYuLhhx/GzJkz8fnnnztNLL744gsIgoDRo0cDAGQyGWQy9zy1KpVKr/rewsJCAGi1JBMA9Ho9/Pz86l1m8ODBeOCBB1rtO5srISEBCQkJDmVPPPEEEhIS8Mgjj9T5ObPZDKvVCoVC0dYh2q1fvx4333yzQ1lSUhLGjRuHzz77zKWJIRE1H6tCEZHbuOWWW/DKK6/g3Llz+PTTT+3lf/75J8aPH4+EhASoVCpERETg0UcfxaVLl+zLzJkzB88//zwAID4+3l7N4+zZswCAlStX4pZbbkFYWBiUSiUSExPxzjvvNBhTbGwsbrrpJqxfvx7V1dW15n/++efo3LkzkpOT7XFc3bZh06ZNuPHGG6HVaqHRaNCtWze8+OKL9vm2Kiu2WG1sVWsyMzPtZb/88gtSU1PRsWNHKJVKxMbGYurUqaisrGxwW65u61Bf9RhbLK2x7521sThz5gxSU1MRHBwMtVqNv/3tb/j++++dbv/atWvx73//GzExMVCpVLj11ltx6tSperd1/PjxGDJkCAAgNTUVEonE4cJ1y5YtGDx4MPz8/KDVajFixAgcPXrUYR22v+WRI0fw8MMPIygoCDfeeGNDu7lOxcXFmD59Onr27AmNRoOAgAAMHz4cf/zxR4Ofraqqwl133YXAwEDs2LEDAGC1WrF48WJce+21UKlUCA8Px+OPP46SkpJGx3T27FlIJBK8/vrrWLx4MTp37gylUokjR44AAI4dO4YHHngAwcHBUKlU6NevH7777rsmb1dmZqb9KU5aWpr9GFm1ahUA1EoqAOC+++4DgFp/FyJyX+55W42IvNaYMWPw4osv4qeffsLEiRMB1FyYnzlzBmlpaYiIiMDhw4fx3nvv4fDhw/jtt98gkUhw//3348SJE/jiiy/w5ptvIiQkBAAQGhoKAHjnnXdw7bXX4p577oFMJsP//d//4amnnoLVasXkyZPrjWn06NGYNGkSNm7ciLvuustefvDgQRw6dAizZs2q87OHDx/GXXfdhV69emHevHlQKpU4deoUtm/f3qz9s27dOhgMBjz55JPo0KEDdu/ejbfffhs5OTlYt25dk9Z1dTUZAHj55ZdRWFhorx7TGvv+agUFBRg4cCAMBgOefvppdOjQAR999BHuuecerF+/3n5BabNgwQJIpVJMnz4dZWVleO211zB69Gjs2rWrzm17/PHHER0djfnz59urJoWHhwMANm/ejOHDhyMhIQFz5sxBZWUl3n77bQwaNAj79u2rVW0pNTUVXbt2xfz58+tta2NTUVGBoqIih7Lg4GCcOXMG33zzDVJTUxEfH4+CggK8++67GDJkCI4cOYKoqCin66usrMSIESPw+++/Y/PmzfYL9McffxyrVq1CWloann76aWRlZWHp0qXYv38/tm/fDrlc3mCsNitXroTRaMSkSZOgVCoRHByMw4cPY9CgQYiOjsaMGTPg5+eHtWvX4t5778WXX35p/zs1Zrt69OiBefPmYdasWZg0aRIGDx4MABg4cGCdMeXn5wOA/XgiIg8gEBG50MqVKwUAwp49e+pcJjAwUOjbt6/9vcFgqLXMF198IQAQtm3bZi9buHChAEDIysqqtbyzdQwbNkxISEhoMObi4mJBqVQKDz30kEP5jBkzBADC8ePH7WWzZ88Wrjy1vvnmmwIA4eLFi3Wu37ZPro5769atAgBh69at9W5Henq6IJFIhHPnztUZhyAIQqdOnYRx48bVGcdrr70mABA+/vjjer+vqfv+6u999tlnBQDCL7/8Yi+rqKgQ4uPjhbi4OMFisThsf48ePYSqqir7skuWLBEACAcPHqxzW678/Lp16xzK+/TpI4SFhQmXLl2yl/3xxx+CVCoVxo4day+z7cOr/+4NfZ+zKSsrSzAajfZts8nKyhKUSqUwb948p3FXVFQIQ4YMEUJCQoT9+/fbl/nll18EAMJnn33msL4NGzY4Lbfx8/Nz+FtkZWUJAISAgAChsLDQYdlbb71V6Nmzp2A0Gu1lVqtVGDhwoNC1a1d7WWO3a8+ePQIAYeXKlc534FUmTJgg+Pj4CCdOnGjU8kQkPlaFIiK3o9FoHHqHurKthdH4/9u78/go6vt/4K9N9s5usgm5DwjIZeQ0SBo8sJoAaqnWCuiXClKLF1gVqUKtINoS6wkVWhQFvEFUpD9FECNoRQTlUJFDCEdIzEEg1+5ms9fn90fchSWbO9mZzb6ej8c83J0r7xmH2XnP57KhoqICv/rVrwAAu3fvbtU+z91HdXU1KioqMHr0aBw9ehTV1dXNbhsdHY1rr70W//3vf2GxWAAAQgisXr0aI0aMQP/+/Zvc1lO/f/369XC73a2KtbXHYbFYUFFRgVGjRkEIgT179rR7v1u2bMHcuXNx77334tZbb/X799p77s+3YcMGjBw50qdakcFgwB133IHjx497q+F4TJs2zae+v+dt99GjR9v8t0tKSrB3717cdtttiImJ8c4fMmQIcnNzsWHDhkbb3HXXXW36G/PmzcPmzZt9psTERGg0Gm8jdpfLhdOnT3urxvk7l9XV1RgzZgwOHjyIrVu3+jR4Xrt2LaKiopCbm4uKigrvlJmZCYPBgC1btrQp5t///vc+JUxnzpzBZ599hokTJ3pLYCoqKnD69GmMHTsWhw8fRnFxMQC0+bha46233sIrr7yCBx98EP369WvXPogo8JhYEJHsmM1mGI1G7/czZ87gvvvuQ0JCAnQ6HeLi4tC7d28AaDEp8Ni2bRtycnK8derj4uK87Rxas4/JkyfDYrFg/fr1ABp6QTp+/Li30XZTJk2ahEsvvRR/+tOfkJCQgJtvvhnvvPNOu5OMwsJC70OxwWBAXFycty1Ba8/F+YqKirxxPvfccz7LOuPcn+/EiRMYMGBAo/kXXnihd/m5evbs6fM9OjoaANrUluDcvw2gyb9fUVHhTR49PMfbWoMHD0ZOTo7PpNVq4Xa78fzzz6Nfv37QaDSIjY1FXFwcvv/+e7/n8v7778c333yDTz/9FBdddJHPssOHD6O6uhrx8fGIi4vzmcxms7fhemudf4xHjhyBEAKPPvpoo/3Pnz8fwNnG8W09rpb873//w+23346xY8fiH//4R5u3JyLpsI0FEclKUVERqqur0bdvX++8iRMn4quvvsJf/vIXDBs2DAaDAW63G+PGjWvVA3pBQQGuvvpqDBw4EM899xzS0tKgVquxYcMGPP/8863ah6fh7FtvvYX/+7//w1tvvYXw8PAWxyfQ6XT44osvsGXLFnz00UfYuHEj1qxZg6uuugqffPIJwsPDmxxQz+VyNfqem5uLM2fO4OGHH8bAgQMRERGB4uJi3Hbbbe1KVux2O2666SZoNBq88847jXq06ui57wzh4eF+54tWtHfoDJ3VO9nChQvx6KOP4o9//COeeOIJxMTEICwsDPfff7/fc3n99ddj9erVePLJJ/Haa6/5dNnrdrsRHx+PN9980+/faqp9S1POP0ZPPLNnz8bYsWP9buP5N9rW42rOd999h9/+9rcYNGgQ3n33Xdn2sEZE/vFfLBHJiqdBsedhprKyEvn5+ViwYIFPI+nDhw832rapB/T/9//+H+rr6/Hf//7X5+13W6qLaDQa3HTTTXjttddQVlaGtWvX4qqrrkJiYmKL24aFheHqq6/G1Vdfjeeeew4LFy7EI488gi1btiAnJ8f7Bv78wcDOf3P/ww8/4KeffsKrr76KKVOmeOdv3ry51cdxvj//+c/Yu3cvvvjiC2/jZo/OOPf+9OrVC4cOHWo0/+DBg97lXcWz76b+fmxsbIvdybbXu+++i1//+td45ZVXfOZXVVX5baB8ww03YMyYMbjttttgNBp9ejG74IIL8Omnn+LSSy/tkm6ZPd3UqlQq5OTkNLtua4+rpWukoKAA48aNQ3x8PDZs2BCw8TWIqPOwKhQRycZnn32GJ554Ar179/ZWMfK8rT7/7fSiRYsabe95IDz/Ad3fPqqrq7Fy5co2xTd58mQ4HA7ceeedOHXqVIvVoICGqkTn89SVr6+vB9DwkAgAX3zxhXcdl8uFl156qcXjEEJg8eLFbToOj5UrV+LFF1/E0qVLMXLkyEbLO+Pc+3Pttddi586d2L59u3eexWLBSy+9hPT0dGRkZLThKNomKSkJw4YNw6uvvuoT6759+/DJJ5/g2muv7bK/HR4e3uhcrl271ttWwZ8pU6bgX//6F5YtW4aHH37YO3/ixIlwuVx44oknGm3jdDo7PGJ1fHw8rrzySrz44osoKSlptPzUqVPez609ruaukdLSUowZMwZhYWHYtGlTm0tciEgeWGJBRJL4+OOPcfDgQTidTpSVleGzzz7D5s2b0atXL/z3v/+FVqsFAERGRuKKK67AU089BYfDgZSUFHzyySc4duxYo31mZmYCAB555BHcfPPNUKlUGD9+PMaMGQO1Wo3x48fjzjvvhNlsxvLlyxEfH+/3oakpo0ePRmpqKtavXw+dTocbb7yxxW0ef/xxfPHFF7juuuvQq1cvlJeX49///jdSU1O9jZcvuugi/OpXv8LcuXNx5swZxMTEYPXq1XA6nT77GjhwIC644ALMnj0bxcXFiIyMxHvvvdeutgYVFRW45557kJGRAY1G4zNuCNAwhkBnnHt/b//nzJmDt99+G9dccw3+/Oc/IyYmBq+++iqOHTuG9957r8tH6X766adxzTXXIDs7G7fffru3u9moqCg89thjXfZ3f/Ob3+Dxxx/HtGnTMGrUKPzwww948803Gw1id76ZM2eipqYGjzzyCKKiovDXv/4Vo0ePxp133om8vDzs3bsXY8aMgUqlwuHDh7F27VosXry4w4P0LV26FJdddhkGDx6M6dOno0+fPigrK8P27dtRVFTkHaeitcd1wQUXwGQyYdmyZTAajYiIiEBWVhZ69+6NcePG4ejRo3jooYfw5Zdf4ssvv/Rul5CQgNzc3A4dCxEFiES9URFRiPJ0reqZ1Gq1SExMFLm5uWLx4sWipqam0TZFRUXid7/7nTCZTCIqKkpMmDBB/PzzzwKAmD9/vs+6TzzxhEhJSRFhYWE+3Z/+97//FUOGDBFarVakp6eLf/7zn2LFihVNdpHalL/85S8CgJg4caLf5ed385qfny+uv/56kZycLNRqtUhOTha33HJLoy40CwoKRE5OjtBoNCIhIUH89a9/FZs3b27U3ez+/ftFTk6OMBgMIjY2VkyfPl189913jbrxbKm7WU83o01NnnPSGefeXze3BQUF4qabbhImk0lotVoxcuRI8eGHH/qs01R3sZ7YW+q2tKnthRDi008/FZdeeqnQ6XQiMjJSjB8/Xuzfv99nHc85bK6r4Nb+PSEaumV98MEHRVJSktDpdOLSSy8V27dvF6NHjxajR49ucT8PPfSQACCWLFninffSSy+JzMxModPphNFoFIMHDxYPPfSQ+Pnnn/3G0FR3s08//bTf9QsKCsSUKVNEYmKiUKlUIiUlRfzmN78R7777bpuPSwgh1q9fLzIyMoRSqfT5f9jctXj+PohIvhRCBKj1GxERERERdVtsY0FERERERB3GxIKIiIiIiDqMiQUREREREXUYEwsiIiIiIuowJhZERERERNRhkicWS5cuRXp6OrRaLbKysrBz585m11+0aBEGDBgAnU6HtLQ0PPDAA7DZbAGKloiIiIiI/JE0sVizZg1mzZqF+fPnY/fu3Rg6dCjGjh2L8vJyv+u/9dZbmDNnDubPn48DBw7glVdewZo1a/DXv/41wJETEREREdG5JB3HIisrC5dccgmWLFkCAHC73UhLS8O9996LOXPmNFp/5syZOHDgAPLz873zHnzwQezYscNnlM7muN1u/PzzzzAajVAoFJ1zIERERERE3ZAQArW1tUhOTkZYWPNlEsoAxdSI3W7Hrl27MHfuXO+8sLAw5OTkYPv27X63GTVqFN544w3s3LkTI0eOxNGjR7FhwwbceuutTf6d+vp61NfXe78XFxcjIyOj8w6EiIiIiKibO3nyJFJTU5tdR7LEoqKiAi6XCwkJCT7zExIScPDgQb/b/N///R8qKipw2WWXQQgBp9OJu+66q9mqUHl5eViwYEGj+SdPnkRkZGTHDoKIiIiIqCtYLEBycsPnn38GIiIkCaOmpgZpaWkwGo0tritZYtEeW7duxcKFC/Hvf/8bWVlZOHLkCO677z488cQTePTRR/1uM3fuXMyaNcv73XNyIiMjmVgQERERkTyFh5/9HBkpWWLh0ZomBJIlFrGxsQgPD0dZWZnP/LKyMiQmJvrd5tFHH8Wtt96KP/3pTwCAwYMHw2Kx4I477sAjjzzit96XRqOBRqPp/AMgIiIiIuoqKhXw1FNnPwcByXqFUqvVyMzM9GmI7Xa7kZ+fj+zsbL/bWK3WRslD+C/ZnIRt0ImIiIiIOpdaDfzlLw2TWi11NK0iaVWoWbNmYerUqRgxYgRGjhyJRYsWwWKxYNq0aQCAKVOmICUlBXl5eQCA8ePH47nnnsPw4cO9VaEeffRRjB8/3ptgEBERERFR4EmaWEyaNAmnTp3CvHnzUFpaimHDhmHjxo3eBt2FhYU+JRR/+9vfoFAo8Le//Q3FxcWIi4vD+PHj8Y9//KPTY3O5XHA4HJ2+X6LOoFKpmEwTERF1Zy4XsHt3w+eLL/ZtcyFTko5jIYWamhpERUWhurrab+NtIQRKS0tRVVUV+OCI2sBkMiExMZHjsRAREXVHFgtgMDR8Npsl7RWquWfncwVVr1CB4Ekq4uPjodfr+dBGsiOEgNVq9Y5Qn5SUJHFEREREREwsfLhcLm9S0aNHD6nDIWqSTqcDAJSXlyM+Pp7VooiIiEhykvUKJUeeNhV6vV7iSIha5rlO2RaIiIiI5ICJhR+s/kTBgNcpERERyQkTC5KF2267DTfccIPUYRARERFROzGx6AYUCkWz02OPPdYlf1dOycCZM2cwefJkREZGwmQy4fbbb4fZbJY6LCIiIqKQwcbb3UBJSYn385o1azBv3jwcOnTIO8/g6aoMDT0KuVwuKJXd63/95MmTUVJSgs2bN8PhcGDatGm444478NZbb0kdGhEREVHbqVTA/PlnPwcBllh0A4mJid4pKioKCoXC+/3gwYMwGo34+OOPkZmZCY1Ggy+//BJutxt5eXno3bs3dDodhg4dinfffde7T5fLhdtvv927fMCAAVi8eLF3+WOPPYZXX30V69ev95aMbN26FQBw8uRJTJw4ESaTCTExMbj++utx/Phxn33PmjULJpMJPXr0wEMPPYSODKdy4MABbNy4ES+//DKysrJw2WWX4YUXXsDq1avx888/t3u/RBQ4ZpsTh0prsbuwEj+V1sJsc0odEhGRpMzuMBy660Hs/uN9+OlMfVDcF7vXa2sZMducKK6qg8XuhEGtRLJJB4NWutM9Z84cPPPMM+jTpw+io6ORl5eHN954A8uWLUO/fv3wxRdf4A9/+APi4uIwevRouN1upKamYu3atejRowe++uor3HHHHUhKSsLEiRMxe/ZsHDhwADU1NVi5ciUAICYmBg6HA2PHjkV2djb+97//QalU4u9//zvGjRuH77//Hmq1Gs8++yxWrVqFFStW4MILL8Szzz6LdevW4aqrrvLGu3DhQixcuLDZY9q/fz969uyJ7du3w2QyYcSIEd5lOTk5CAsLw44dO/C73/2ua04qEXWKokorNu8vQ5X1bA9nJr0KuRkJSI1mL31EFHqC9b7IxKILyPFiePzxx5GbmwsAqK+vx8KFC/Hpp58iOzsbANCnTx98+eWXePHFFzF69GioVCosWLDAu33v3r2xfft2vPPOO5g4cSIMBgN0Oh3q6+uRmJjoXe+NN96A2+3Gyy+/7O21aOXKlTCZTNi6dSvGjBmDRYsWYe7cubjxxhsBAMuWLcOmTZt84r3rrrswceLEZo8pOTkZQMOghvHx8T7LlEolYmJiUFpa2p7TRUQBYrY5G90vAaDK6sDm/WWYkJkm6UsZIqJA894XzfXoUVgAADjd84KguC/KM6ogJtcfyXPf5h85cgRWq9WbaHjY7XYMHz7c+33p0qVYsWIFCgsLUVdXB7vdjmHDhjX7d7777jscOXIERqPRZ77NZkNBQQGqq6tRUlKCrKws7zKlUokRI0b4VIeKiYlBTExMew6ViIJIcVVdo/ulR5XVgeKqOgxINPpdTkTUHXnui8p6G6bc8RsAwAvr98Cp08v+vsjEopPJ9UcyIiLC+9nTW9JHH32ElJQUn/U0Gg0AYPXq1Zg9ezaeffZZZGdnw2g04umnn8aOHTua/TtmsxmZmZl48803Gy2Li4trdbxtqQqVmJiI8vJyn2VOpxNnzpzxKU0hIvmx2JuvM2xtYTkRUXcTzPdFJhadLBguhoyMDGg0GhQWFmL06NF+19m2bRtGjRqFe+65xzuvoKDAZx21Wg2Xy+Uz7+KLL8aaNWsQHx+PyMhIv/tOSkrCjh07cMUVVwBoSAJ27dqFiy++2LtOW6pCZWdno6qqCrt27UJmZiYA4LPPPoPb7fYpGSEi+YlQN/8zpG9hORFRdxPM90X5RhakguFiMBqNmD17Nh544AG43W5cdtllqK6uxrZt2xAZGYmpU6eiX79+eO2117Bp0yb07t0br7/+Or755hv07t3bu5/09HRs2rQJhw4dQo8ePRAVFYXJkyfj6aefxvXXX4/HH38cqampOHHiBN5//3089NBDSE1NxX333Ycnn3wS/fr1w8CBA/Hcc8+hqqrKJ8a2VIW68MILMW7cOEyfPh3Lli2Dw+HAzJkzcfPNN3uTDyKSpxSTDia9ym9Jr0mvQopJJ0FURETS8dwXzXWNl8n9vsjuZjuZ52LwR04XwxNPPIFHH30UeXl53gfzjz76yJs43HnnnbjxxhsxadIkZGVl4fTp0z6lFwAwffp0DBgwACNGjEBcXBy2bdsGvV6PL774Aj179sSNN96ICy+8ELfffjtsNpu3BOPBBx/ErbfeiqlTp3qrWXW056Y333wTAwcOxNVXX41rr70Wl112GV566aUO7ZOIup5Bq0RuRkKj+6anwwu5NlAkIuoqwXxfVIiODCAQhGpqahAVFYXq6upGVXVsNhuOHTuG3r17Q6vVtvtvyLFXKOp+Out6JZIDTxfdVrsTerUSKRJ30U1EJDXz6WoYYk0AgJ8KSpCcHCvJfbG5Z+fz8a7dBVKj9ZiQmcYfSSKiVjJolbLt5YSISArnPjf2TzACQfAcKf8IgxR/JImIiIio3VQqYPbss5+DABOLAHO5BRwuN1xugfAwBVThYQgPU0gdFhERERHJiVoNPP201FG0CROLALI7XaixOeFyn23WEh6mQKRWCbUyXMLIiIiIiIg6hr1CBYjLLRolFc3NJyIiIqIQ5nYDx483TG631NG0CkssAsRT/ckfT/Wo8DCWWhARERERgLo6wDN+mNkMRERIG08rsMQiQFoqkXCzxIKIiIiIghgTiwBpqYF2GBtwExEREVEQY2IRIM31/uTpHYqIiIiIKFjxaTZAPL0/nZ9cNDU/1Nx222244YYbpA6DiIiIiNqJiUUAqZXhiNarEaVTwahRIkqnQrRe3eGuZhUKRbPTY4891jkHcB45JQP/+Mc/MGrUKOj1ephMJqnDISIiIgo57BUqwMLDFJ3e+1NJSYn385o1azBv3jwcOnTIO89gMHg/CyHgcrmgVHav//V2ux0TJkxAdnY2XnnlFanDISIiIgo5LLHoBhITE71TVFQUFAqF9/vBgwdhNBrx8ccfIzMzExqNBl9++SXcbjfy8vLQu3dv6HQ6DB06FO+++653ny6XC7fffrt3+YABA7B48WLv8sceewyvvvoq1q9f7y0Z2bp1KwDg5MmTmDhxIkwmE2JiYnD99dfj+PHjPvueNWsWTCYTevTogYceeghCdKxXrAULFuCBBx7A4MGDO7QfIiIiIllQKoF77mmYguSFcHBEGYzqa4Gqk4DdDGgMQFQaoDFKFs6cOXPwzDPPoE+fPoiOjkZeXh7eeOMNLFu2DP369cMXX3yBP/zhD4iLi8Po0aPhdruRmpqKtWvXokePHvjqq69wxx13ICkpCRMnTsTs2bNx4MAB1NTUYOXKlQCAmJgYOBwOjB07FtnZ2fjf//4HpVKJv//97xg3bhy+//57qNVqPPvss1i1ahVWrFiBCy+8EM8++yzWrVuHq666yhvvwoULsXDhwmaPaf/+/ejZs2eXnjciIiIiSWg0wNKlUkfRJkwsukJlIXBoA1BXeXaeLhoYcC0QLc2D8OOPP47c3FwAQH19PRYuXIhPP/0U2dnZAIA+ffrgyy+/xIsvvojRo0dDpVJhwYIF3u179+6N7du345133sHEiRNhMBig0+lQX1+PxMRE73pvvPEG3G43Xn75ZSgUDQ3SV65cCZPJhK1bt2LMmDFYtGgR5s6dixtvvBEAsGzZMmzatMkn3rvuugsTJ05s9piSk5M7fmKIiIiIqFMwsehs9bWNkwqg4fuhDcDwyZKUXIwYMcL7+ciRI7Bard5Ew8Nut2P48OHe70uXLsWKFStQWFiIuro62O12DBs2rNm/89133+HIkSMwGn2P0WazoaCgANXV1SgpKUFWVpZ3mVKpxIgRI3yqQ8XExCAmJqY9h0pEREQU/IQAKioaPsfGAgr59yDKxKKzVZ1snFR41FU2LE/ICGxMACLOGQbebDYDAD766COkpKT4rKfRaAAAq1evxuzZs/Hss88iOzsbRqMRTz/9NHbs2NHs3zGbzcjMzMSbb77ZaFlcXFyr42VVKCIiIgppVisQH9/w2WwGznmWkysmFp3Nbm5+ucMSmDiakZGRAY1Gg8LCQowePdrvOtu2bcOoUaNwzz33eOcVFBT4rKNWq+FyuXzmXXzxxVizZg3i4+MRGRnpd99JSUnYsWMHrrjiCgCA0+nErl27cPHFF3vXYVUoIiIiouDCxKKzqQ3NL1dJn20ajUbMnj0bDzzwANxuNy677DJUV1dj27ZtiIyMxNSpU9GvXz+89tpr2LRpE3r37o3XX38d33zzDXr37u3dT3p6OjZt2oRDhw6hR48eiIqKwuTJk/H000/j+uuvx+OPP47U1FScOHEC77//Ph566CGkpqbivvvuw5NPPol+/fph4MCBeO6551BVVeUTY1urQhUWFuLMmTMoLCyEy+XC3r17AQB9+/b16W6XiIiIiLoGE4vOZkpraKjtrzqULrphuQw88cQTiIuLQ15eHo4ePQqTyYSLL74Yf/3rXwEAd955J/bs2YNJkyZBoVDglltuwT333IOPP/7Yu4/p06dj69atGDFiBMxmM7Zs2YIrr7wSX3zxBR5++GHceOONqK2tRUpKCq6++mpvCcaDDz6IkpISTJ06FWFhYfjjH/+I3/3ud6iurm738cybNw+vvvqq97unrYgnJiIiIiLqWgrR0QEEgkxNTQ2ioqJQXV3dqKqOzWbDsWPH0Lt3b2i12vb/kaZ6hRp4LWBimwDqHJ12vRIREZH8WCyAp9aFhG0smnt2Ph9LLLpCdM+G3p+qTja0qVBFNJRUSDiOBRERERFRV2Ji0VU0Rkl6fyIiIiIikgITCyIiIiIiuVEqgalTz34OAsERJRERERFRKNFogFWrpI6iTcKkDoCIiIiIiIIfSyyIiIiIiORGiIbRtwFArwcUCmnjaQWWWBARERERyY3V2tDdrMFwNsGQOSYWRERERETUYUwsiIiIiIiow5hYEBERERFRh8kisVi6dCnS09Oh1WqRlZWFnTt3NrnulVdeCYVC0Wi67rrrAhixvPg7H+dOjz32WJf83dtuuw033HBDl+y7PVatWgWTydSq9TznJjw8HNHR0cjKysLjjz+O6urqNv3N48ePQ6FQYO/eve0L+hx5eXm45JJLYDQaER8fjxtuuAGHDh3q8H6JiIiIAkHyxGLNmjWYNWsW5s+fj927d2Po0KEYO3YsysvL/a7//vvvo6SkxDvt27cP4eHhmDBhQoAjl49zz8eiRYsQGRnpM2/27NnedYUQcDqdEkYrD55zVFRUhK+++gp33HEHXnvtNQwbNgw///yzJDF9/vnnmDFjBr7++mts3rwZDocDY8aMgcVikSQeIiIiojYREhs5cqSYMWOG97vL5RLJyckiLy+vVds///zzwmg0CrPZ3Kr1q6urBQBRXV3daFldXZ3Yv3+/qKura13wMrRy5UoRFRXl/b5lyxYBQGzYsEFcfPHFQqVSiS1btgiXyyUWLlwo0tPThVarFUOGDBFr1671bud0OsUf//hH7/L+/fuLRYsWeZfPnz9fAPCZtmzZIo4dOyYAiDVr1ojLLrtMaLVaMWLECHHo0CGxc+dOkZmZKSIiIsS4ceNEeXm5T+zLly8XAwcOFBqNRgwYMEAsXbrUu8yz3/fee09ceeWVQqfTiSFDhoivvvrK5zjPnebPn9+qc+RRVlYmYmNjxeTJk73zPv74Y3HppZeKqKgoERMTI6677jpx5MgR7/Lz/+bo0aNbdTytUV5eLgCIzz//3O/y7nC9EhERURPMZiEaOp1t+CyR5p6dzydpYlFfXy/Cw8PFunXrfOZPmTJF/Pa3v23VPgYNGiSmT5/e5HKbzSaqq6u908mTJ9uXWJjNTU/nr9/culZr69Ztp6YSiyFDhohPPvlEHDlyRJw+fVr8/e9/FwMHDhQbN24UBQUFYuXKlUKj0YitW7cKIYSw2+1i3rx54ptvvhFHjx4Vb7zxhtDr9WLNmjVCCCFqa2vFxIkTxbhx40RJSYkoKSkR9fX13gTAs+/9+/eLX/3qVyIzM1NceeWV4ssvvxS7d+8Wffv2FXfddZc3zjfeeEMkJSWJ9957Txw9elS89957IiYmRqxatUoIIXz2++GHH4pDhw6Jm266SfTq1Us4HA5RX18vFi1aJCIjI73x1NbWtuocneu+++4TRqNROJ1OIYQQ7777rnjvvffE4cOHxZ49e8T48ePF4MGDhcvlEkIIsXPnTgFAfPrpp6KkpEScPn26VcfTGocPHxYAxA8//OB3ORMLIiKibqyuToibbmqYJPytD5rEori4WADwvnX2+Mtf/iJGjhzZ4vY7duwQAMSOHTuaXMffm/V2JRaejNHfdO21vuvq9U2ve84bbSGEELGx/tdrp6YSiw8++MA7z2azCb1e3+i833777eKWW25pct8zZswQv//9773fp06dKq6//nqfdTwJwMsvv+yd9/bbbwsAIj8/3zsvLy9PDBgwwPv9ggsuEG+99ZbPvp544gmRnZ3d5H5//PFHAUAcOHDA77E3pbn1/vOf/wgAoqyszO/yU6dO+Tzse+Las2ePz3otHU9LXC6XuO6668Sll17a5DpMLIiIiKirtSWxCOqRt1955RUMHjwYI0eObHKduXPnYtasWd7vNTU1SEtLC0R4sjJixAjv5yNHjsBqtSI3N9dnHbvdjuHDh3u/L126FCtWrEBhYSHq6upgt9sxbNiwVv29IUOGeD8nJCQAAAYPHuwzz9OOxmKxoKCgALfffjumT5/uXcfpdCIqKqrJ/SYlJQEAysvLMXDgwFbF1RIhBICGBvEAcPjwYcybNw87duxARUUF3G43AKCwsBCDBg3yu4+2HE9TZsyYgX379uHLL7/syOEQERERBYykiUVsbCzCw8NRVlbmM7+srAyJiYnNbmuxWLB69Wo8/vjjza6n0Wig0Wg6HCvM5qaXhYf7fm+i4TkAIOy89vLHj7c7pLaIiIjwfjb/ciwfffQRUlJSfNbznKvVq1dj9uzZePbZZ5GdnQ2j0Yinn34aO3bsaNXfU6lU3s+eh/Tz53ke0j3xLF++HFlZWT77CT/v3Prbr2c/neHAgQOIjIxEjx49AADjx49Hr169sHz5ciQnJ8PtdmPQoEGw2+1N7qMtx+PPzJkz8eGHH+KLL75AampqB46GiIiIKHAkTSzUajUyMzORn5/v7bbU7XYjPz8fM2fObHbbtWvXor6+Hn/4wx8CECmAcx7MJVu3k2RkZECj0aCwsBCjR4/2u862bdswatQo3HPPPd55BQUFPuuo1Wq4XK4Ox5OQkIDk5GQcPXoUkydPbvd+OhpPeXk53nrrLdxwww0ICwvD6dOncejQISxfvhyXX345ADQqQVCr1QDg83fbezxCCNx7771Yt24dtm7dit69e7f7WIiIiCjIWSyAwdDw2WyW5JmxrSSvCjVr1ixMnToVI0aMwMiRI7Fo0SJYLBZMmzYNADBlyhSkpKQgLy/PZ7tXXnkFN9xwg/fNMrWe0WjE7Nmz8cADD8DtduOyyy5DdXU1tm3bhsjISEydOhX9+vXDa6+9hk2bNqF37954/fXX8c033/g87Kanp2PTpk04dOgQevTo0epqPv4sWLAAf/7znxEVFYVx48ahvr4e3377LSorK32qsjUnPT0dZrMZ+fn5GDp0KPR6PfR6vd91hRAoLS2FEAJVVVXYvn07Fi5ciKioKDz55JMAgOjoaPTo0QMvvfQSkpKSUFhYiDlz5vjsJz4+HjqdDhs3bkRqaiq0Wi2ioqLadTwzZszAW2+9hfXr18NoNKK0tBQAEBUVBZ1O19pTSURERCSNLm7v0SovvPCC6Nmzp1Cr1WLkyJHi66+/9i4bPXq0mDp1qs/6Bw8eFADEJ5980ua/FardzVZWVvqs53a7xaJFi8SAAQOESqUScXFxYuzYsd6uTW02m7jttttEVFSUMJlM4u677xZz5swRQ4cO9e6jvLxc5ObmCoPB0Ki72XMbM/uLwV8D6jfffFMMGzZMqNVqER0dLa644grx/vvvCyH8N5KurKz0/l2Pu+66S/To0aPF7mbxSyN+hUIhoqKixMiRI8Xjjz/e6LrYvHmzuPDCC4VGoxFDhgwRW7duFQB8ejJbvny5SEtLE2FhYT7dzTZ3PP54Yjp/Wrlypd/1u8P1SkRERE0Iwu5mFUL80lo1RNTU1CAqKgrV1dWIjIz0WWaz2XDs2DH07t0bWq1WogiJWofXKxERUTcmk6pQzT07n0/ykbeJiIiIiCj4MbEgIiIiIqIOY2JBREREREQdJnmvUEREREREdJ7wcODaa89+DgJMLIiIiIiI5EarBT76SOoo2oSJhR8h1lEWBSlep0RERN2X2eZEcVUdLHYnDGolkk06GLTyfnSXd3QBplKpAABWq5UDkpHsWa1WAGevWyIiIuoeiiqt2Ly/DFVWh3eeSa9CbkYCUqP9D/4rB0wszhEeHg6TyYTy8nIAgF6vh0KhkDgqIl9CCFitVpSXl8NkMiE8SOpdEhERUcvMNic27y+D+XQ1Zk4cBQBY9s5XqIIem/eXYUJmmmxLLuQZlYQSExMBwJtcEMmVyWTyXq9EwS4Yi/yJiLpCcVUdqqwOKAGo6ut8llVZHSiuqsOARKM0wbWAd+3zKBQKJCUlIT4+Hg6Ho+UN2shS70R5TT2sDif0KiXiIzWI0PB/A7WNSqViSQV1G8Fa5E9E1BUsdmezy60tLJcSn2ibEB4e3ukPbg0/nqf440lE9AtPkf+590Wg4a2c3Iv8iYi6QoS6+XuevoXlUuIAeQHS0o+n2Sbf7JOIqKt4ivz98RT5ExGFkhSTDia9/45ZTHoVUkzy7WCIiUWA8MeTiKixYC7yJyLqCgatErkZCY2SC08tFzmX4so3sm6GP55ERI0Fc5E/EVFXSY3W43fDU73fxw5KRHJyrKyTCoCJRcDwx5OIqDFPkb+/El25F/kTEXWpsDBYsy+DSwgoFMFRyYhPswHCH08iosY8Rf5N9Qol97dzRERdoaHDnwpULXilYcaRKph+tsi+wx+FEEJIHUQg1dTUICoqCtXV1YiMjAzo32aXikRE/nnGsbDandCrlUjhOBZEFKLMNifW7jrZ5MvoQPeW15ZnZ961Ayg1Wo8JmWn88SQiOo9Bq5TtgE9ERIHUmg5/5Hq/5BNtgPHHk4iIiIia4unwR1lnxe1TrgIAvPLaZ3DqGmq3yLnDHyYWREREREQycW6HP/rqykbL5dzhT3A0MSciIiIiCgEcII+IiIiIiDqMA+RRq3l6PrHYnTColUhm420iIiIiOgcHyKMWsbtZIiIiImqNc5OI/glGQOZJBcCqUAFjtjkbJRVAQ7dhm/eXwWyTbwt/IqKuZrY5cai0FrsLK/FTaS3viUREQUj+qU83Ecx9EhMRdSWW5hIR+REWBowYcfZzEAiOKLsBSwt9Dsu5T2Iioq7C0lwioibodMA33zRMOvn2BHUuJhYBEtFCn8Ny7pOYiKirtKY0l4iIggMTiwAJ5j6JiYi6CktziYi6DyYWARLMfRITEXUVluYSETXBagXS0xsmq1XqaFqFd+wASo3WY0JmGoqr6mC1O6FXK5HCcSyIKIR5SnP9VYdiaS4RhTQhgBMnzn4OAnyiDTCDVsnen4iIfuEpzW2qVyi+eCEiCh68YxMRkaRYmktE1D3wrk1ERJJjaS4RUfBj420iIiIiIuowJhZERERERNRhrApFRERERCQ3CgWQkXH2cxBgYkFEREREJDd6PfDjj1JH0SasCkVERERERB3GxIKIiIiIiDqMiQURERERkdxYrcBFFzVMVqvU0bQK21gQEREREcmNEMD+/Wc/BwGWWBARERERUYcxsSAiIiIiog5jYkFERERERB3GxIKIiIiIiDqMiQUREREREXWY5InF0qVLkZ6eDq1Wi6ysLOzcubPZ9auqqjBjxgwkJSVBo9Ggf//+2LBhQ4CiJSIiIiIKAIUC6NWrYVIopI6mVSTtbnbNmjWYNWsWli1bhqysLCxatAhjx47FoUOHEB8f32h9u92O3NxcxMfH491330VKSgpOnDgBk8kU+OCJiIiIiLqKXg8cPy51FG2iEEK6jnGzsrJwySWXYMmSJQAAt9uNtLQ03HvvvZgzZ06j9ZctW4ann34aBw8ehEqlatffrKmpQVRUFKqrqxEZGdmh+ImIiIiIurO2PDtLVhXKbrdj165dyMnJORtMWBhycnKwfft2v9v897//RXZ2NmbMmIGEhAQMGjQICxcuhMvlavLv1NfXo6amxmciIiJ5MducOFRai92FlfiptBZmm1PqkIiIqI0kqwpVUVEBl8uFhIQEn/kJCQk4ePCg322OHj2Kzz77DJMnT8aGDRtw5MgR3HPPPXA4HJg/f77fbfLy8rBgwYJOj7+9zDYniqvqYLE7YVArkWzSwaDlAOhEFLqKKq3YvL8MVVaHd55Jr0JuRgJSo/USRkZEJB1zZS3Cfz0abgH8/MFGJCXFyP6ZUd7RncftdiM+Ph4vvfQSwsPDkZmZieLiYjz99NNNJhZz587FrFmzvN9ramqQlpYWqJB98MeTiMiX2eZsdF8EgCqrA5v3l2FCZprsf0iJiDpbUaUVW3YV4tbv9gAANv7wMww/W2T/zChZVajY2FiEh4ejrKzMZ35ZWRkSExP9bpOUlIT+/fsjPDzcO+/CCy9EaWkp7Ha73200Gg0iIyN9Jim09OPJYn8iCkXFVXWosjpgd7px2lyPkuo6nDbXw+50o8rqQHFVndQhEhEFVDA/M0qWWKjVamRmZiI/P987z+12Iz8/H9nZ2X63ufTSS3HkyBG43W7vvJ9++glJSUlQq9VdHnNHeH48/eGPJxGFKovdiRqbA/tLqnG43IwTp604XG7G/pJq1NgcsNrl+wNKRNQVPM+MDtfZ590zluB44SLpOBazZs3C8uXL8eqrr+LAgQO4++67YbFYMG3aNADAlClTMHfuXO/6d999N86cOYP77rsPP/30Ez766CMsXLgQM2bMkOoQWs3Swo8jfzyJKBSpwsJw9JQZNofbZ77N4cbRU2YowyQfbomIKKA8L1wOlJ7tcKjglCUoXrhIWnF10qRJOHXqFObNm4fS0lIMGzYMGzdu9DboLiwsRNg5PyppaWnYtGkTHnjgAQwZMgQpKSm477778PDDD0t1CK0WoW7+VOtbWE5E1B2pwhWI0qpgc9Q3WhalVUEVHhyDQhERdRbPCxcRhC9cJH+anTlzJmbOnOl32datWxvNy87Oxtdff93FUXW+FJMOJr3Kb3Uok16FFJNOgqiIiKRV53Dh0r6x2HakAmW1Z5OLBKMGl/aNhc3RdHfiRETdkeeFS5W58TK5v3CRPLEIFQatErkZCdjwfQkKz1hhd7mhDg9Dzxg9cjMS2OsJEYUkvVqJ0hobRvaOgQBQ73RDowyDAkBpjQ3DekZLHSIRUUB5Xrh8Y6tDjcHknR8ML1z4NBtgcUYNdOpw74+nQcP/BUQUulJMOkTqVDhlPtuzX+0v/2VpLhGFIs8Ll2EXpmD9J3tQ73QjN0heuPCpNkD8dR1WC6DCbEdVnYN9tRNRSPKU5jY1xg/vi0QUaoL5hQvv2AHSmu5mByQaAxwVEZH0UqP1mJCZhuKqOljtTujVSqSYdEwqiCgkBfMLF/lG1s2wu1kioqYZtEq+XCEi+kVqtB4TMmIRdt21cAmBkrfeR3JSjKyTCoCJRcBEqJUIUwA9ItQNDRQdbmjU4VAIgdMWO7ubJSIiIqKz3G7ot38JACgV7hZWlgc+zQZIikmH9NgI5O8va9Sl4tUZCbKuL0dE1NXMNieKq+pgsTthUCuRzKpQRBTCiiqt2LKnCLf+8n3jvlIYSuqQm5GA1Gi9pLE1h3ftACo8Y0G1zbedRbXNgcIzFokiIiKSXlGltcm6xHL+ASUi6gqeDn8qz3kRfcZSD6uqHpv3l8m6wx95RtUNFVfVwekCMpKiUGtzwOFyQxUeBqNWBacLbLxNRCHJX495QEOnFnL/ASUi6grFVXUoPGNFUWmNd17BKQsUdYDNaZD1MyPv1gHiabytVoahh0HTaDkbbxNRKGKPeUREvqqsdhw9ZYZw+LarsDncOHrKjGqrvYktpRcmdQChIqKFxtlsvE1EoYg95hER+XILAZvDDZdbeOdZ7U643L/MF6KZraXFxCJAUkw6mPQqv8vkPtgJEVFX4UsXIiJferUS0XoVymttqFNpUKfSoLzWhrIaG6L1KlnfF+UbWTcTzIOdEBF1Fc9LF3/VofjShYhCUbhCgb7xBhSesWLk3A+889O0SvSNNyBcoZAuuBbwaTaAOLosEZEvz0uX/+79GQWnzLA5XNCqwnFBnIEvXYgoZO05WYVeMXoM72mC0yWgDFfgjNmOPSerMO6iJKnDaxLv2BIRAOSbbxIRBU5NnQNOlxtxRg0cLgFVuAJOlxs1dQ4gWuroiIgCq7zWhmGpJuw8dgbfF1d75ydH6TCydwzKa20AoqQLsBlMLAKIfbUTEfk6VVuPlduOo/CMtdGyk5V1eGjcQMQZG/ekR0TUXYWHK7DnZBUGxaiRt3IuhAA++Nti1LjDsedkFbL6xEgdYpOYWASI2eZE/oEyqMIUiDWoUe9wQ6MOh0II5B8ow+8vZl/tRBR6jpTX+k0qAKDwjBVHymuZWBBRSEkwahEboUZBWRX6fvMFAOCHE2dQr9EhwahBvFErcYRN45NsgBRX1UGrDMe2IxUoO2ckxQSjBpf2jWVf7UQUkqrr/I9h4VFTx+5miSi0pEbrcXVGAv63u85nfoJRg6tlXsuFiUWA2ByuRkkFAJTV1mPbkQoMTIqUKDIiIulE6fx3w+0RqePPFBGFFoNWicxe0VBYLN551wxKhNYUicxe0bKu4SLfyLoZq93ZKKnwKKut5yBQRBSS+sYb0TNG77c6VM8YPfrGsySXiEJParQepoEJ3u+Z6TFITo6VdVIBcIC8gAlTKKBV+T/dWlWYrPskJiLqKnFGDW67NB09Y3yL9nvG6HHbpelsX0FEIevcJKJ/glH2SQXAEouAMenV6BNnwNFTZtgcbu98rSoMfeIMiNKrJYyOiEg6FyVH4f6cfjhUWovqOgeidCoMSDQiRcb1iImIqDEmFgGSYtKhZ4weWmU4am0OOFxuqMLDYNSqEB+p4eiyRBSy/HXFfeKMlV1xExEFGVaFChDP6LLxkRr0MGiQGKVDD4MG8ZEaji5LRCHLbHM2SioAoMrqwOb9ZTDb2P6MiEJURAQgRMMUESF1NK3Cp9kASo3WY0JmGoqr6mC1O6FXK5Fi0jGpIKKQVVxV1yip8KiyOtgVNxFREOETbYAZtEr+SBIR/cLSQo947DGPiCh4MLEIsFO19ThS3tBA0aRT4YJ4I3s9IaKQFaFu/mdI38JyIqJuy2YDbr214fPrrwNa+Y647cE7dgD9+HM1Vm077tNfu6dLxYuSoySMjIhIGikmHUx6ld/qUCa9ih1bEFHocrmAd99t+LxqlaShtBYbbwfIqdr6RkkFABSesWLVtuM41cTgeURE3ZmnYwuT3ncEbpNexY4tiIiCDO/YAXKkvNbvyLJAQ3JxpLyWVaKIKCSxYwsiosbMNicMv3w+XFaLpGSN7O+L8o6uG6mu89/riUdNHRsoElHoYscWRERnFVVasWVPEX5pYYGN+0phKKmT/fg+rAoVIFE6VbPLI3XM8YiIiIhCXTCP78PEIkD6xhvRM8Z/htkzRo++8XxTR0RERBTqWjO+j1zxNXmAxBk1mHZpOj7dXwarwwWHS0AdHgadKgw5GQlsX0FEREREQT2+DxOLAIrUqaAMD8OpM1bUO9zQqMJwQZwBkS1UkyIiIiKi0OAZ38ep1eGF9Xu8nz3kPL4Pq0IFiKe+XL3TjdRoPS6INyA1Wo96p1v29eWIiIiIKDA84/tAoYBTp4dTpwcUCgDyH9+HiUWABHN9OSKirma2OXGotBa7CyvxU2ktX7YQUcjyjO8ToQ7HaXM9SqrrcNpcjwh1uOzH95FvZN1MMNeXIyLqSkWVVmz4vgSFZ6ywu9xQh4ehZ4we1w5JknW3ikREXSlBA1z98gK43ALfzFkIfRC0x2ViESARLdSHk3N9OSKirmK2ObFuTxG+PV4Jm8PtnX+y0op6lwvTRvWR9ds5IqLO5qk+bz5di+s3vAcA2HT3oyi3K1BV58CEzDTZ3hdZFSpAvPXl/JB7fTkioq5yrMLSKKkAAJvDjW+PV+JYhUWiyIiIpBHM1eeZWASIp77c+cmFSa+SfX05IqKuUl5ra5RUeNgcbpTX2gIcERGRtIK5+jyfZgMoNVqPCZlpKK6qg9XuhF6tRIpJx6SCiEKWMlzR7HJVC8uJiLqbYK4+L9/IuimDVokBiRxlm4gIABKMWiQYNSirrfezTIN4o1aCqIiIpOOpPm/2U+NJ7tXnWRWKiIgkkxqtx9UZCUg4r7eTBKMGV2cksFcoIgo5wVx9Xr6RERFRt2fQKpHZKxput4C53ol6pxsaZRgMmob5cv4BJSLqKqnRevxueKr3+9hBiUhOjpX9PVHe0RERUbeXGq2HSadm+zMionMYYiKB8nIAQP/YWO/o23LGuzYREUmO7c+IiM6jUABxcVJH0SayaGOxdOlSpKenQ6vVIisrCzt37mxy3VWrVkGhUPhMWi0b9xERERERSUnyxGLNmjWYNWsW5s+fj927d2Po0KEYO3Ysyn8p+vEnMjISJSUl3unEiRMBjJiIiIiIqIvV1wMzZjRM9Y17zpMjyROL5557DtOnT8e0adOQkZGBZcuWQa/XY8WKFU1uo1AokJiY6J0SEhICGDERERERURdzOoF//7thcsp3ULxzSZpY2O127Nq1Czk5Od55YWFhyMnJwfbt25vczmw2o1evXkhLS8P111+PH3/8scl16+vrUVNT4zMREREREVHnkjSxqKiogMvlalTikJCQgNLSUr/bDBgwACtWrMD69evxxhtvwO12Y9SoUSgqKvK7fl5eHqKiorxTWlpapx8HEREREVGok7wqVFtlZ2djypQpGDZsGEaPHo33338fcXFxePHFF/2uP3fuXFRXV3unkydPBjhiIiIiIqLuT9LuZmNjYxEeHo6ysjKf+WVlZUhMTGzVPlQqFYYPH44jR474Xa7RaKDRaPwuIyIiIiKiziFpiYVarUZmZiby8/O989xuN/Lz85Gdnd2qfbhcLvzwww9ISkrqqjCJiIiIiKgFkg+QN2vWLEydOhUjRozAyJEjsWjRIlgsFkybNg0AMGXKFKSkpCAvLw8A8Pjjj+NXv/oV+vbti6qqKjz99NM4ceIE/vSnP0l5GEREREREIU3yxGLSpEk4deoU5s2bh9LSUgwbNgwbN270NuguLCxEWNjZgpXKykpMnz4dpaWliI6ORmZmJr766itkZGRIdQhERERERJ1LpwOOHTv7OQgohBBC6iACqaamBlFRUaiurkZkZKTU4RARERERyVZbnp2DrlcoIiIiIiKSHyYWRERERERyY7cDf/lLw2S3Sx1Nq7AqFBERERGR3FgsgMHQ8NlsBiIiJAmDVaGIiIiIiCigmFgQEREREVGHMbEgIiIiIqIOY2JBREREREQdxsSCiIiIiIg6jIkFEREREZHMmG1O7+fDZbU+3+VKKXUARERERER0VlGlFZv3VyD8pQ8BAKcPV8FUUofcjASkRusljq5pTCwCzGxzoriqDha7Ewa1EskmHQxa/m8gIiIiooZnxc37y1BlcwHp/bzzq6wObN5fhgmZabJ9duxQVEeOHEFBQQGuuOIK6HQ6CCGgUCg6K7ZupyH7LEOV1eGdZ9KrZJ99EhEREVFgFFfV+TwrnqvK6kBxVR0GJBoDHFXrtKuNxenTp5GTk4P+/fvj2muvRUlJCQDg9ttvx4MPPtipAXYX3uzzvAvFk30GQ705IiIiIupaFnvDM2GYw45fvfYCfvXaCwhz2L3LrXb5PjO2K7F44IEHoFQqUVhYCL3+7Jv2SZMmYePGjZ0WXHfSmuyTiIiIiEJbhLqhQlGY04nsN5Yg+40lCHOeTSb0anlWgwLaWRXqk08+waZNm5Camuozv1+/fjhx4kSnBNbdWFrILuWcfRIRERFRYKSYdDDpVTD7eeds0quQYtIFPqhWaldiYbFYfEoqPM6cOQONRtPhoLqjiBaySzlnn0REREQUGAatErkZCdi9/2xNl1ijBtooPS7pHSPbhttAO6tCXX755Xjttde83xUKBdxuN5566in8+te/7rTgupMUkw6xBhX6xkWgZ4wOPSLU6NlDj75xEYg1yDv7JCLqamabE4dKa7G7sBI/lQZHf+1ERF2porbe+/mn0hqcOue7XLUr5Xnqqadw9dVX49tvv4XdbsdDDz2EH3/8EWfOnMG2bds6O8ZuwaBVIiM5Cv/+rAAHy2q88wcmROKeqy6QdfZJRNSViiqt2PB9CQrPWGF3uaEOD0PPGD2uHZLEHvOIKOR4Ovyx2F3eeTERGljsru7Z3eygQYPw008/YcmSJTAajTCbzbjxxhsxY8YMJCUldXaM3cKp2nqs3nkS1TYHYiLUcLsFwsIUqLY5sHrnSfSMiUCckdXIiCi0mG1OrNtThG+PV8LmcHvnn6y0ot7lwrRRfWT7A0pE1BU8Hf74u/PJvbvZdt2tCwsLkZaWhkceecTvsp49e3Y4sO7mSHktCs9YER6maNSeovCMFUfKa5lYEFHIOVZhaZRUAIDN4ca3xytxZX8LBqdGSRQdEVHgBXOHP+1KLHr37o2SkhLEx8f7zD99+jR69+4Nl8vVxJahq7rOf1ezHjV18r1IiIi6SnmtrVFS4WFzuFFeawPAxIKIQoenwx+XWoO3Xljr/ewh5w5/2hVZUyNsm81maLXaDgfVHUXpVM0uj9TJ9yIhIuoqyvDGvyXnUrWwnIiou/F0N1tlBcoGDPFZ1q26m501axaAhl6gHn30UZ8uZ10uF3bs2IFhw4Z1aoDdRd94I3rG6FF4xtpoWc8YPfrGy7OuHBFRV0owapFg1KDMT28nCUYN4o18WUVEocXT3ezm/WU+gyub9CrkZiTIut1ZmyLbs2cPgIYSix9++AFqtdq7TK1WY+jQoZg9e3bnRthNxBk1uO3SdKzadtwnuegZo8dtl6azfQURhaTUaD2uzkhA/v4yn+QiwajB1RkJ7BWKiEJSarQeEwYnwPrMc3A4XTDfNRMp8VGyTioAQCGEEG3daNq0aVi8eDEiIyO7IqYuVVNTg6ioKFRXV0sS/6naehwpr0VNnROROiX6xhuZVBBRSCuqtOKbY2dgrnei3umGRhkGg0aJS3rHMLEgotBlsQAGQ8NnsxmIiJAkjLY8O7cr7Vm5cmW7AqOGkgsmEkREZ6VG62HSqVFcVQer3Qm9WokUk072b+aIiMhXu+/a3377Ld555x0UFhbCbrf7LHv//fc7HBgREYUOg1Yp237ZiYikYLY58Ut5BQ6X1SIpWSP7Fy5h7dlo9erVGDVqFA4cOIB169bB4XDgxx9/xGeffYaoKHYLSERERETUXkWVVqzbU+T9vnFfKdbuOomiysadAMlJuxKLhQsX4vnnn8f/+3//D2q1GosXL8bBgwcxceJEDo5HRERtZrY5cai0FrsLK/FTaS3MNo7tQ0ShyWxzNuoRCmgYdXvz/jJZ3x/bVZ5SUFCA6667DkBDb1AWiwUKhQIPPPAArrrqKixYsKBTgyQiou6rqNLaZLeKbLxNRKGmuKoOVVaH34f0KqsDxVV1sq062q4Si+joaNTW1gIAUlJSsG/fPgBAVVUVrFZ5F9EQEZF8BPObOSKirmCxN3/fs7awXErtKrG44oorsHnzZgwePBgTJkzAfffdh88++wybN2/GVVdd1dkxEhFRN+V5M+eP3N/MERF1hQh1w+O5S63B2qdf83720Kvl24C7XZEtWbIENpsNAPDII49ApVLhq6++wu9//3sOkEdERK0WzG/miIi6QopJB5NehfIaN767YBjsLjfUdU4YtQrER2qQYtJJHWKT2lUVKiYmBsnJyQ07CAvDnDlz8M477yA5ORnDhw/v1ACJiKj7imjhzZuc38wREXUFg1aJkb1jUGGux+FyM06ctuJwuRkV5nqM7B0j6y5n25RY1NfXY+7cuRgxYgRGjRqFDz74AEDDgHkXXHABFi9ejAceeKAr4iQiom7I82bOH5NeJes3c0REXcFsc+Lb42cwLFGPWYc3488HP8H4jFgMTY3Ct8fPyLrtWZtSnnnz5uHFF19ETk4OvvrqK0yYMAHTpk3D119/jWeffRYTJkxAeHh4V8VKRETdjEGrRG5GQpO9Qsn5zRwRUVcorqrDGYsDyjorsp6dDwDY/evr4dTpvcvl2vasTXfstWvX4rXXXsNvf/tb7Nu3D0OGDIHT6cR3330HhULRVTESEVE3lhqtx4TMNBRX1cFqd0KvViLFpGNSQUQhKZjbnrXprl1UVITMzEwAwKBBg6DRaPDAAw8wqWgDs82J4qo6WOxOGNRKJPPHk4gIBq1Stm/giIgCKZjbnrUpMpfLBbVafXZjpRIGg6HTg+quOAgUERERETXH0/bMXNd4mdzbnrUpsRBC4LbbboNG09CXrs1mw1133YWIiAif9d5///3Oi7CbaGkQqAmZaSy5ICIiIgpxnrZnW3b5DjodDG3P2hTZ1KlTfb7/4Q9/6NRgujMOAkVERERErZEarcfvhqd6v48dlIjk5FhZJxVAGxOLlStXdlUc3V4wN8QhIupqbH9GROTr3Htg/wQjEAT3RPlH2E0Ec0McIqKuxPZnRER+aDTAhx+e/RwE2jXyNrUdB4EiImqspfZnch4IioioSymVwHXXNUzK4HgBzcQiQDwNcc5PLoKhIQ4RUVdpTfszIqJQZLY5cai0FrsLK/FTaW1QvGjh02wAcRAoIiJfbH9GRNRYUaUVn35fhKQPG3pa/d9V4xEZqZd9FVGWWEhEAOCwgkQU6tj+jIjIl6eKaG21FWOfmYuxz8xFmMMRFFVEZZFYLF26FOnp6dBqtcjKysLOnTtbtd3q1auhUChwww03dG2AnaSo0oq1u05iww8l+PzQKXz0QwnW7jqJokpryxsTEXVDbH9GROQrmKuISp5YrFmzBrNmzcL8+fOxe/duDB06FGPHjkV5eXmz2x0/fhyzZ8/G5ZdfHqBIO4YNFImIGvO0P0vvoUesQQ2jRolYowbpPfRsf0ZEISmYq4hKnlg899xzmD59OqZNm4aMjAwsW7YMer0eK1asaHIbl8uFyZMnY8GCBejTp08Ao22/YM4+iYi62qnaehwqrcXh8locKqnBqdp6qUMiIpJEMFcRlTSxsNvt2LVrF3JycrzzwsLCkJOTg+3btze53eOPP474+HjcfvvtLf6N+vp61NTU+ExSCObsk4ioq3hKcy12F3oYNEiM0qGHQQOL3cXSXCIKSZ4qonWOs/e/n3/p+EfuVUQlTSwqKirgcrmQkJDgMz8hIQGlpaV+t/nyyy/xyiuvYPny5a36G3l5eYiKivJOaWlpHY67PYI5+yQi6ioszSUi8mXQKjEkNQrHTp1tg7vz+GkcLbdgaGqUrKuISl4Vqi1qa2tx6623Yvny5YiNjW3VNnPnzkV1dbV3OnnyZBdH6R8bKBIRNcbSXCIiX6dq67H2myIkRZ0dbfvawUlINmnxzjdFsq4qKmnKExsbi/DwcJSVlfnMLysrQ2JiYqP1CwoKcPz4cYwfP947z+12AwCUSiUOHTqECy64wGcbjUYDjQyGQfc0UNzwfQkKz1hhd7mhDg9Dzxg2UCSi0MXSXCIiX0fKa3HstAVhLieen/53AMC3JVa4w+3e5XFG6Z9t/ZH0jq1Wq5GZmYn8/Hxvl7Futxv5+fmYOXNmo/UHDhyIH374wWfe3/72N9TW1mLx4sWSVXNqizijBjp1OOqdbmiUYTBo+KNJRKHLU5rrrzoUS3OJKBRV1zXcD93hSnydeVWj5TV18i3JlfypdtasWZg6dSpGjBiBkSNHYtGiRbBYLJg2bRoAYMqUKUhJSUFeXh60Wi0GDRrks73JZAKARvPlxl93s7UAKsx2VNU5MCEzjaUWRBRyPKW5598fTXoVS3OJKCRF6fxXnfeI1Mn3vih5ZJMmTcKpU6cwb948lJaWYtiwYdi4caO3QXdhYSHCwoKqKYhfrWmgOCDRGOCoiIiklxqtx2+GJONIeS1q6pyI1CnRN94o26J+IqKu1DfeiJ4xehSdqsHIvV8AAHYOuwLucCV6xujRN16+z4sKIYSQOohAqqmpQVRUFKqrqxEZGRmwv7u7sBKfHzrV5PIrB8RheM/ogMVDRCQXRZXWJkssUqP1EkZGRCSNH3+uxpv5B7BwSjYAYMrifCQk9cBtl6bjouSogMbSlmdnyUssQgUbKBIRNeavmijQUJK7eX8Zq4kSUUi6KDkKD+T2936f8esL0Cc9UfYlubxbBwgbKBIRNVZcVYeaOgfiDGoIAPUONzTqcCiEwGmLndVEiShknZtEZPWJBSLknVQATCwChg0UiYgas9qdSIzUYtuRCpSd0zd7glGDS/vGoo7jWBARBQ0+zQZQarQeEzLTUPzLsOx6tRIpJh2TCiIKWTpVeKOkAgDKauux7UgFhqaZpAmMiIjaLPi7WwpSAoBC6iCIiCTmcAlU2/z3mFdtc8DhCqn+RYiIghpflQcQez4hIvLlcLvRJ86Ao6fMsDnc3vlaVRj6xBngdLub2ZqIiOSEiUWAsOcTIqLGItRKRGpVyEiKQq3NAYfLDVV4GIxaFdTKMPaYR0ShS60GVq48+zkI8I4dIBwgj4iosXN7zOth8O3xhD3mEVFIU6mA226TOoo2YRuLALG00LOJlT2fEFEI8vSYZ9KrfOazxzwiouDDO3aAcIA8IiL/2GMeEZEfTiewaVPD57FjAaX874nyj7Cb4AB5RERNM2iVrA5KRHSu+nrgN79p+Gw2B0ViwapQAcLifiKippltThwqrcXuwkr8VFoLs43VQ4mIgg2fZgOIxf1ERI2xK24iou6BT7QBxuJ+IqKz2BU3EVH3wapQREQkmdZ0xU1ERMGBiQUREUmGXXETEXUfTCyIiEgy7IqbiKj74B2biIgkw664iYiaoFYDS5ac/RwEmFgQEZFkPF1xN9UrFBtuE1HIUqmAGTOkjqJNeMcmIiJJsStuIqLugXdtIiKSHLviJiI6j8sF/O9/DZ8vvxwID5c2nlZgYkFEREREJDPmKjMMv/41AOBwQQmSkmNlX5LLXqGIiIiIiGSkqNKKdXuKvN837ivF2l0nUVRplTCqljGxICIiIiKSCbPN2ahDC6Bh0NDN+8tgtsl3fB8mFkREREREMlFcVee3C26gIbkorqoLcEStx8SCiIiIiEgmLPaGEgmHy+2dd8ZSD7uz4bvVLt8SC3m3ACEiIiIiCiERaiVqbA4UldZ45xWcskBRB/SJM0Cvlu/jO0ssiIiIiIhkIiZCDbPNiXqH22e+zeGG2eZETIR8R+GWb8pDRERERBRizljsGNErGl/X2fDGjQ0jbzvDlUgwajCiVzTOWOyIM2okjtI/JhYBZrY5UVxVB4vdCYNaiWSOLktEREREv7DYnSitsSGzXwLE7Nmod7pxjTIMCgClNTa2saAGRZXWRt2HmfQq5GYkIDVaL2FkRERERCQHEWol3AI4ZbZ759Wes5xtLCio+yQmIiIiosBIMelg0qugcLmQcOh7JBz6HgqXC0DDC+kUk07iCJvGxCJAiqvqUFPnQJxBjViDGkaNErFGDeIMatTUybtPYiIiIiIKDINWidyMBPRQuvF/907A/907AeH2em8tFzlXoZdvZN2M1e5EYqQW245UoKy23js/wajBpX1jUSfj+nJERF2N7c+IiM5Kjdbjd8NTvd/HDkpEcnKs7O+L8o6uG9GpwhslFQBQVluPbUcqMDTNJE1gREQSY/szIqLGzk0i+icYAZknFQCrQgWMwyVQbfM/PHu1zQGHSwQ4IiIi6bH9GRFR98HEIkAcbjf6xBmgVfmecq0qDH3iDHC63U1sSUTUfRVX1TVKKjyqrGx/RkQUTORfptJNRKiViNSqkJEUhVqbAw6XG6rwMBi1KqiVYbLuOoyIqKtYWmhfJuf+2omIyBefZgPE03VYldWBHgbf0RLl3nUYEVFXiWjhpQpfuhARBQ/esQPE03VYUw0U5d7Kn4ioK5z70uV8fOlCRCFNpQLmzz/7OQgohBAh1Wq4pqYGUVFRqK6uRmRkZMD/vqdLRavdCb1aiRR2qUhEIY69QhERyVdbnp35RBtgBq0SAxKNUodBRCQbqdF6/GZIMo6U16KmzolInRJ9442IM2pa3piIiGSDiQUREUnKX4nFwdJallgQUWhzu4EDBxo+X3ghECb/zlzlH2E3Y7Y5cai0FrsLK/FTaS37aCeikMZxLIiImlBXBwwa1DDVBUfX2yyxCCDWIyYi8tWacSxYfZSIKDiwxCJAPG/lymvqcdpcj5LqOpw216O8pp5v5YgoZHEcCyIi/859NjxcFhy1XFhiESDFVXUoPGPF0VNm2BxnR9nWqsJgcxr4Vo6IQhLHsSAiaqyo0oote4pw6y/fN+4rhaGkTva1XGRRYrF06VKkp6dDq9UiKysLO3fubHLd999/HyNGjIDJZEJERASGDRuG119/PYDRtk+V1d4oqQAAm8ONo6fMqLbaJYqMiEg6nnEs/OE4FkQUioK57ZnkicWaNWswa9YszJ8/H7t378bQoUMxduxYlJeX+10/JiYGjzzyCLZv347vv/8e06ZNw7Rp07Bp06YAR942biEaJRUeNocbrtAaToSICMDZwUPPTy44eCgRharWtD2TK8nv2M899xymT5+OadOmAQCWLVuGjz76CCtWrMCcOXMarX/llVf6fL/vvvvw6quv4ssvv8TYsWMDEXK76NVKJBg1KKutb7QswahhcT8RhazUaD0mZKZx8FAiIgR32zNJ79p2ux27du3C3LlzvfPCwsKQk5OD7du3t7i9EAKfffYZDh06hH/+859+16mvr0d9/dmH+Zqamo4H3g5aVTgu7RuLbUcqfJKLBKMGl/aNhVYVLklcRERywMFDiYgaeNqe2RCG/10/FW63QIXNDb3KDbUyTNYvoyWNrKKiAi6XCwkJCT7zExIScPDgwSa3q66uRkpKCurr6xEeHo5///vfyM3N9btuXl4eFixY0Klxt0eKSYevj1ZgZO8YCAD1Tjc0yjAoANicLtYjJiIiIiKkmHRQhgN7K+rw7TV3NsysrIfW7MCI9GhZPzNK3saiPYxGI/bu3YtvvvkG//jHPzBr1ixs3brV77pz585FdXW1dzp58mRgg/2FQavE1RcmwOEWqDDbUWtzosJsh8MtcPWFrEdMRERERA16xkQgSuvb9ixKq0LPmAiJImodSZ9mY2NjER4ejrKyMp/5ZWVlSExMbHK7sLAw9O3bFwAwbNgwHDhwAHl5eY3aXwCARqOBRqPp1Ljbi/WIiYiIiKg5xVV1OF5hwcheJujLfobd6YYjJRWKsDAcr7DIeogCSUss1Go1MjMzkZ+f753ndruRn5+P7OzsVu/H7Xb7tKOQM0894uE9ozEg0cikgoiIiIi8LHYn3AKoPF2DG39/OW6eNBpVp2twymyHW7DxdrNmzZqFqVOnYsSIERg5ciQWLVoEi8Xi7SVqypQpSElJQV5eHoCGNhMjRozABRdcgPr6emzYsAGvv/46/vOf/0h5GERE1AFmmxPFVXWw2J0wqJVIZmkuEYWoYB44VPLIJk2ahFOnTmHevHkoLS3FsGHDsHHjRm+D7sLCQoSFnS1YsVgsuOeee1BUVASdToeBAwfijTfewKRJk6Q6BCIi6oCiSmujwaA841jIeYRZIqKu4Bk41OxnuAq5DxyqECK0RmarqalBVFQUqqurERkZKXU4REQhzWxzYu2uk34HgzLpVZiQmcaSCyIKOUWVVmzZdQy35g4CALywfg8MPaIkeeHSlmdn3q2JiEgyrRlhVq6NFImIukpqtB6/G57q/T52UCKSk2Nl/6JF3tEREVG3FswjzBIRdaVzk4j+CUZA5kkFEKTjWBARUfcQzI0UiYjIF+/YREQkGU8jxabaWMi5kSIRUZdSKoF77jn7OQgER5RERNQtGbRK5GYkNNkrlNzrExMRdR07MG8GYDcD1QVAVBqgkXebM96xiYhIUqnRekwaEo26U8fhstUiXBsJXVw89EZ2NUtEIaqyEDi0AairPDtPFw0MuBaI7ildXC1gYkFERNKqLIT+0Aboz/0BLZf/DygRUZeor21IKqxngGpLw7yoiIYk49AGYPhk2ZZcsPE2ERFJx/MDem5SAZz9Aa2vlSYuIiKpVJ1suAfaHMCNCxsm2y9VResqG5bLFBMLIiKSjucH1B+Z/4ASEXUJu7n55Q5LYOJoB1aFCjCzzYniqjpY7E4Y1Eokm3RsnEhEoSuIf0CJiLqE2tD8clVEYOJoBz7RBlBRpRXfHDsDc70T9Q43NOpwGNThuKR3TMCHZycikoUg/gElIuoSprSGhtp1ZY2X6aIblssUE4sAMduc2HWiEp/uL0NhpRUut0B4mAI9o/UIC1PApFOz5IKIQo/3B9RPdSiZ/4ASEXUJjbGh84q963zn66KBgdfKtuE2wMQiYIoqrfj4hxIcKKmB0y2882vqHHAJgQEJRgxMipQwQiIiCfzyA1q//yPUnimDw+WGOjwMhpgEaGT+A0pE1GWiewJDJwG4v+H7wOuAlAGyvycysQiQkuq6RkkFADjdAgdKalBSXcfEgohCUhFicUCfi8jwUoQ76+BS6lCjScSFIhapUgdHRCSVc5OIhAsBjfyrhjKxCBCr3dUoqfBwugWsdleAIyIikp7Z5vxl1G03gPizC2rdKLKWYUJmGquJElFoUiqBqVPPfg4CwRFlNxCpVSFCrYTF7my0LEKtRKRWJUFURETSKq6qQ5XV4XdZldWB4qo6DEiUd9E/EVFXMItwFD/5QkNPopV2JJvCZf+iRd7RdSNxRg0ye0Vj14lKn+QiQq1EZq9oxBk1EkZHRCQNfy9bzmVtYTkRUXdUVGn9pTT37IsXk16F3IwEWfckysQiQFKj9ci+oAfcQqC8th5Ot4AyTIF4owbZF/SQ9UVCRNRVItTN/wzpW1hORNTdeKuIWuxQ2uoAAE6tDlVWBzbvl3cVUXlG1Q0ZtEpc3CsaLrdoGMfC6YZGGQaDpmG+XC8QIqKulGLSwaRX+a0OZdKrkGLSSRAVEZF0PFVElbY63Hv9cADAC+v3wKnTy76KKJ9mAyg1Wg+TTo3iqjpY7U7o1UqkcORtIgphBq0SuRkJTRb58/5IRKEmmKuI8o4dYAatUrZZJhGRFFKj9ZiQmcaXLkRECO4qovKNjIiIQgZfuhARNfBUETXXNV4m9yqiYVIHQEREREREDTxVRE1636EIgqGKqHwjIyIiIiIKQanRevxueKr3+9hBiUhOjpV1UgEwsSAiIiIikp1zk4j+CUZA5kkFwMSCiIiIiEh+wsOBm246+zkIMLEgIiIiIpIbrRZYu1bqKNqEjbeJiIiIiKjDmFgQEREREVGHMbEgIiIiIpIbiwVQKBomi0XqaFqFiQUREREREXUYEwsiIiIiIuowJhZERERERDJjtjm9nw+X1fp8lysmFkREREREMlJUacW6PUXe7xv3lWLtrpMoqrRKGFXLmFgQEREREcmE2ebE5v1lqLI6fOZXWR3YvL9M1iUXTCyIiIiIiGSiuKquUVLhUWV1oLiqLsARtR5H3iYiIiIikgmLvaFEQoSH4+jI0d7PHla7fEssmFgQEREREclEhLrh8dyl1mD9319qtFyvlu/jO6tCERERERHJRIpJB5Ne5XeZSa9CikkX4Ihaj4kFEREREZFMGLRK5GYkNEouTHoVcjMSYNDKt8RCvpEREREREYWg1Gg9JgyMgT4tGQJAwb4CJCfHyjqpAJhYEBERERHJjkGrBOoaxq3on2AEZJ5UAEwsiIhIBsw2J4qr6mCxO2FQK5Fs0sn+zRwREfniXZuIiCRVVGltNBiUpy5xarRewsiIiKgt2HibiIgkE8wjzBIRkS8mFkREJJlgHmGWiIh8MbEgIiLJWFoYQVbOI8wSEZEvWSQWS5cuRXp6OrRaLbKysrBz584m112+fDkuv/xyREdHIzo6Gjk5Oc2uT0RE8hXRwgiych5hloioS4WFAaNHN0xhsnhkb5HkUa5ZswazZs3C/PnzsXv3bgwdOhRjx45FeXm53/W3bt2KW265BVu2bMH27duRlpaGMWPGoLi4OMCRExFRRwXzCLNERF1KpwO2bm2YdMFxL1QIIYSUAWRlZeGSSy7BkiVLAAButxtpaWm49957MWfOnBa3d7lciI6OxpIlSzBlypQW16+pqUFUVBSqq6sRGRnZ4fiJiKhj2CsUEZF8teXZWdIyZrvdjl27dmHu3LneeWFhYcjJycH27dtbtQ+r1QqHw4GYmBi/y+vr61FfX+/9XlNT07GgiYioU6VG6zEhMw3FVXWw2p3Qq5VI4TgWRERBR9KqUBUVFXC5XEhISPCZn5CQgNLS0lbt4+GHH0ZycjJycnL8Ls/Ly0NUVJR3SktL63DcRETUuQxaJQYkGjG8ZzQGJBqZVBARWSxAXFzDZLFIHU2rSN7GoiOefPJJrF69GuvWrYNWq/W7zty5c1FdXe2dTp48GeAoiYiIiIjaxmxzAhUVQEUFDpfVBsW4PpK+EoqNjUV4eDjKysp85peVlSExMbHZbZ955hk8+eST+PTTTzFkyJAm19NoNNBoNJ0SLxERERFRVyuqtGLLniLc+sv3jftKYSipk33bM0lLLNRqNTIzM5Gfn++d53a7kZ+fj+zs7Ca3e+qpp/DEE09g48aNGDFiRCBCJSIiIiLqcmabs1GHFkDDoKGb95fJuuRC8qpQs2bNwvLly/Hqq6/iwIEDuPvuu2GxWDBt2jQAwJQpU3wad//zn//Eo48+ihUrViA9PR2lpaUoLS2F2WyW6hCIiIiIiDpFcVVdo6TCo8rqQHFVXYAjaj3JW8dNmjQJp06dwrx581BaWophw4Zh48aN3gbdhYWFCDtnUJD//Oc/sNvtuOmmm3z2M3/+fDz22GOBDJ2IiIiIqFNZ7M2XSFhbWC4lyRMLAJg5cyZmzpzpd9nWrVt9vh8/frzrAyIiIiIikkCEuvnHc30Ly6Uk38iIiIiIiEJMikkHk16F2vowlPYfBAAQv9TeMelVSDHJdxRuJhZERERERDJh0CqRm5GAzfuBt5e8551v0quQm5Eg63F+5BsZEREREVEISo3WY0JmGoqr6mC1O6FXK5Fi0sk6qQCYWBARERERyY5Bq8SARKPUYbSJ5N3NEhERERHReaxWID29YbJapY6mVVhiQUREREQkN0IAJ06c/RwEWGJBREREREQdxsSCiIiIiIg6jIkFERERERF1GBMLIiIiIiLqMCYWRERERETUYewVioiIiIhIbhQKICPj7OcgwMSCiIiIiEhu9Hrgxx+ljqJNWBWKiIiIiIg6jIkFERERERF1GKtCBZjZ5kRxVR0sdicMaiWSTToYtPzfQERERETnsFqBSy5p+PzNNw1Vo2SOT7QBVFRpxeb9ZaiyOrzzTHoVcjMSkBot/4uFiIiIiAJECGD//rOfgwCrQgWI2eZslFQAQJXVgc37y2C2OSWKjIiIiIio45hYBEhxVV2jpMKjyupAcVVdgCMiIiIiIuo8rAoVIBZ78yUS1haWExF1Z2x/RkQU/HjXDpAIdfOnWt/CciKi7ortz4iIugdWhQqQFJMOJr3K7zKTXoUUky7AERERSY/tz4iIug8mFgFi0CqRm5HQKLnwvJVjkT8RhSK2PyMiaoJCAfTq1TApFFJH0yp8mg2g1Gg9JmSmobiqDla7E3q1EimsR0xEIYztz4iImqDXA8ePSx1Fm/CJNsAMWiUGJBqlDoOISBbY/oyIqPtgVSgiIpIM258REXUfTCyIiEgybH9GRNSEujrgkksaprrgaG/GOzYREUmK7c+IiPxwu4Fvvz37OQjwrk1ERJJj+zMiouDHqlBERERERDJz7jg+h8tqg2JcHyYWREREREQyUlRpxbo9Rd7vG/eVYu2ukyiqtEoYVcuYWBARERERyYTZ5sTm/WWNBg+tsjqweX+ZrEsu2MaCiIgkZ7Y5UVxVB4vdCYNaiWQ23iaiEFVcVYcqq8PvQ3qV1YHiqjrZtknjXTvA+ONJROSrqNLa6O2cp7vZ1Gi9hJEREQWexX62RMIaFd1oudXOEgsCfzyJiM7XUpH/hMw0vnwhopASoW645zl1ery49utGy/Vq+d4T2cYiQIK5vhwRUVfxFPn74ynyJyIKJSkmXaNBQz1MehVSTLoAR9R6TCwChD+eRESNWVoo0pdzkT8RUVcwaJXIzUholFx4arnIuRRXvpF1M/zxJCJqLKKFIn05F/kTEXWV1Gg9JmTEIuy6a+ESAiVvvY/kpBhZJxUAE4uA4Y8nEVFjniJ/fyW6ci/yJyLqSgZ1GLD9SwCAMT4CkHlSAbAqVMAEc305IqKuEsxF/kRE5It37ADx/Hg21SsUfzyJKFSlRusxITMNxVV1sNqd0KuVSGFX3EREQYd37QDijycRkX8GrVK2Az4REVHr8Ik2wPjjSURERETdEdtYEBERERFRh7HEgoiIiIhIjvR6qSNoEyYWRERERERyExEBWCxSR9EmrApFREREREQdJnlisXTpUqSnp0Or1SIrKws7d+5sct0ff/wRv//975Geng6FQoFFixYFLlAiIiIiImqSpInFmjVrMGvWLMyfPx+7d+/G0KFDMXbsWJSXl/td32q1ok+fPnjyySeRmJgY4GiJiIiIiALEZgOuu65hstmkjqZVFEIIIdUfz8rKwiWXXIIlS5YAANxuN9LS0nDvvfdizpw5zW6bnp6O+++/H/fff3+b/mZNTQ2ioqJQXV2NyMjI9oZORERERNR1LBbAYGj4bDY3tLmQQFuenSUrsbDb7di1axdycnLOBhMWhpycHGzfvr3T/k59fT1qamp8JiIiIiIi6lySJRYVFRVwuVxISEjwmZ+QkIDS0tJO+zt5eXmIioryTmlpaZ22byIiIiIiaiB54+2uNnfuXFRXV3unkydPSh0SEREREVG3I9k4FrGxsQgPD0dZWZnP/LKysk5tmK3RaKDRaDptf0RERERE1JhkJRZqtRqZmZnIz8/3znO73cjPz0d2drZUYRERERERUTtIOvL2rFmzMHXqVIwYMQIjR47EokWLYLFYMG3aNADAlClTkJKSgry8PAANDb7379/v/VxcXIy9e/fCYDCgb9++rfqbnk6w2IibiIiIiGTr3FG3a2oAl0uSMDzPzK3qSFZI7IUXXhA9e/YUarVajBw5Unz99dfeZaNHjxZTp071fj927JgA0GgaPXp0q//eyZMn/e6DEydOnDhx4sSJEydO/qeTJ0+2+Jwt6TgWUnC73fj5559hNBqhUCgkiaGmpgZpaWk4efIkx9LoAJ7HjuM57Bw8j52D57HjeA47B89j5+B57Dg5nEMhBGpra5GcnIywsOZbUUhaFUoKYWFhSE1NlToMAEBkZCT/oXUCnseO4znsHDyPnYPnseN4DjsHz2Pn4HnsOKnPYVRUVKvW6/bdzRIRERERUddjYkFERERERB3GxEICGo0G8+fP5/gaHcTz2HE8h52D57Fz8Dx2HM9h5+B57Bw8jx0XbOcw5BpvExERERFR52OJBRERERERdRgTCyIiIiIi6jAmFkRERERE1GFMLDroiy++wPjx45GcnAyFQoEPPvigxW22bt2Kiy++GBqNBn379sWqVasarbN06VKkp6dDq9UiKysLO3fu7PzgZaSt5/H9999Hbm4u4uLiEBkZiezsbGzatMlnncceewwKhcJnGjhwYBcehbTaeg63bt3a6PwoFAqUlpb6rMdr8YNm17/tttv8nseLLrrIu06oXYt5eXm45JJLYDQaER8fjxtuuAGHDh1qcbu1a9di4MCB0Gq1GDx4MDZs2OCzXAiBefPmISkpCTqdDjk5OTh8+HBXHYbk2nMely9fjssvvxzR0dGIjo5GTk5Oo3+z/q7ZcePGdeWhSKo953HVqlWNzpFWq/VZJ5Sux/acwyuvvNLvvfG6667zrhNq1+J//vMfDBkyxDsmRXZ2Nj7++ONmtwm2+yITiw6yWCwYOnQoli5d2qr1jx07huuuuw6//vWvsXfvXtx///3405/+5PNQvGbNGsyaNQvz58/H7t27MXToUIwdOxbl5eVddRiSa+t5/OKLL5Cbm4sNGzZg165d+PWvf43x48djz549PutddNFFKCkp8U5ffvllV4QvC209hx6HDh3yOUfx8fHeZbwWW7Z48WKf83fy5EnExMRgwoQJPuuF0rX4+eefY8aMGfj666+xefNmOBwOjBkzBhaLpcltvvrqK9xyyy24/fbbsWfPHtxwww244YYbsG/fPu86Tz31FP71r39h2bJl2LFjByIiIjB27FjYbLZAHFbAtec8bt26Fbfccgu2bNmC7du3Iy0tDWPGjEFxcbHPeuPGjfO5Ht9+++2uPhzJtOc8Ag0Dkp17jk6cOOGzPJSux/acw/fff9/n/O3btw/h4eGN7o2hdC2mpqbiySefxK5du/Dtt9/iqquuwvXXX48ff/zR7/pBeV8U1GkAiHXr1jW7zkMPPSQuuugin3mTJk0SY8eO9X4fOXKkmDFjhve7y+USycnJIi8vr1PjlavWnEd/MjIyxIIFC7zf58+fL4YOHdp5gQWR1pzDLVu2CACisrKyyXV4Lbb9Wly3bp1QKBTi+PHj3nmhfC0KIUR5ebkAID7//PMm15k4caK47rrrfOZlZWWJO++8UwghhNvtFomJieLpp5/2Lq+qqhIajUa8/fbbXRO4zLTmPJ7P6XQKo9EoXn31Ve+8qVOniuuvv74LIgwOrTmPK1euFFFRUU0uD/XrsT3X4vPPPy+MRqMwm83eeaF+LQohRHR0tHj55Zf9LgvG+yJLLAJs+/btyMnJ8Zk3duxYbN++HQBgt9uxa9cun3XCwsKQk5PjXYcac7vdqK2tRUxMjM/8w4cPIzk5GX369MHkyZNRWFgoUYTyNWzYMCQlJSE3Nxfbtm3zzue12D6vvPIKcnJy0KtXL5/5oXwtVldXA0Cjf5/nauneeOzYMZSWlvqsExUVhaysrJC5HltzHs9ntVrhcDgabbN161bEx8djwIABuPvuu3H69OlOjVXOWnsezWYzevXqhbS0tEZvlUP9emzPtfjKK6/g5ptvRkREhM/8UL0WXS4XVq9eDYvFguzsbL/rBON9kYlFgJWWliIhIcFnXkJCAmpqalBXV4eKigq4XC6/65xf953OeuaZZ2A2mzFx4kTvvKysLKxatQobN27Ef/7zHxw7dgyXX345amtrJYxUPpKSkrBs2TK89957eO+995CWloYrr7wSu3fvBgBei+3w888/4+OPP8af/vQnn/mhfC263W7cf//9uPTSSzFo0KAm12vq3ui51jz/DdXrsbXn8XwPP/wwkpOTfR48xo0bh9deew35+fn45z//ic8//xzXXHMNXC5XV4QuK609jwMGDMCKFSuwfv16vPHGG3C73Rg1ahSKiooAhPb12J5rcefOndi3b1+je2MoXos//PADDAYDNBoN7rrrLqxbtw4ZGRl+1w3G+6JSkr9K1IneeustLFiwAOvXr/dpH3DNNdd4Pw8ZMgRZWVno1asX3nnnHdx+++1ShCorAwYMwIABA7zfR40ahYKCAjz//PN4/fXXJYwseL366qswmUy44YYbfOaH8rU4Y8YM7Nu3r1u3KQmE9pzHJ598EqtXr8bWrVt9Gh7ffPPN3s+DBw/GkCFDcMEFF2Dr1q24+uqrOzVuuWnteczOzvZ5izxq1ChceOGFePHFF/HEE090dZiy1p5r8ZVXXsHgwYMxcuRIn/mheC0OGDAAe/fuRXV1Nd59911MnToVn3/+eZPJRbBhiUWAJSYmoqyszGdeWVkZIiMjodPpEBsbi/DwcL/rJCYmBjLUoLB69Wr86U9/wjvvvNOouPB8JpMJ/fv3x5EjRwIUXfAZOXKk9/zwWmwbIQRWrFiBW2+9FWq1utl1Q+VanDlzJj788ENs2bIFqampza7b1L3Rc615/huK12NbzqPHM888gyeffBKffPIJhgwZ0uy6ffr0QWxsLK/HZqhUKgwfPtx7jkL1emzPObRYLFi9enWrXqKEwrWoVqvRt29fZGZmIi8vD0OHDsXixYv9rhuM90UmFgGWnZ2N/Px8n3mbN2/2vhlRq9XIzMz0WcftdiM/P7/JOnih6u2338a0adPw9ttv+3Rf1xSz2YyCggIkJSUFILrgtHfvXu/54bXYNp9//jmOHDnSqh/P7n4tCiEwc+ZMrFu3Dp999hl69+7d4jYt3Rt79+6NxMREn3VqamqwY8eObns9tuc8Ag29xDzxxBPYuHEjRowY0eL6RUVFOH36NK/HZrhcLvzwww/ecxRq12NHzuHatWtRX1+PP/zhDy2u292vRX/cbjfq6+v9LgvK+6IkTca7kdraWrFnzx6xZ88eAUA899xzYs+ePeLEiRNCCCHmzJkjbr31Vu/6R48eFXq9XvzlL38RBw4cEEuXLhXh4eFi48aN3nVWr14tNBqNWLVqldi/f7+44447hMlkEqWlpQE/vkBp63l88803hVKpFEuXLhUlJSXeqaqqyrvOgw8+KLZu3SqOHTsmtm3bJnJyckRsbKwoLy8P+PEFQlvP4fPPPy8++OADcfjwYfHDDz+I++67T4SFhYlPP/3Uuw6vxZbPo8cf/vAHkZWV5XefoXYt3n333SIqKkps3brV59+n1Wr1rnPrrbeKOXPmeL9v27ZNKJVK8cwzz4gDBw6I+fPnC5VKJX744QfvOk8++aQwmUxi/fr14vvvvxfXX3+96N27t6irqwvo8QVKe87jk08+KdRqtXj33Xd9tqmtrRVCNFzfs2fPFtu3bxfHjh0Tn376qbj44otFv379hM1mC/gxBkJ7zuOCBQvEpk2bREFBgdi1a5e4+eabhVarFT/++KN3nVC6HttzDj0uu+wyMWnSpEbzQ/FanDNnjvj888/FsWPHxPfffy/mzJkjFAqF+OSTT4QQ3eO+yMSigzxddp4/TZ06VQjR0JXa6NGjG20zbNgwoVarRZ8+fcTKlSsb7feFF14QPXv2FGq1WowcOVJ8/fXXXX8wEmrreRw9enSz6wvR0I1vUlKSUKvVIiUlRUyaNEkcOXIksAcWQG09h//85z/FBRdcILRarYiJiRFXXnml+Oyzzxrtl9diy/+mq6qqhE6nEy+99JLffYbatejv/AHwudeNHj3a59+rEEK88847on///kKtVouLLrpIfPTRRz7L3W63ePTRR0VCQoLQaDTi6quvFocOHQrAEUmjPeexV69efreZP3++EEIIq9UqxowZI+Li4oRKpRK9evUS06dP79YvC9pzHu+//37vfS8hIUFce+21Yvfu3T77DaXrsb3/pg8ePCgAeB+czxWK1+If//hH0atXL6FWq0VcXJy4+uqrfc5Nd7gvKoQQopMKP4iIiIiIKESxjQUREREREXUYEwsiIiIiIuowJhZERERERNRhTCyIiIiIiKjDmFgQEREREVGHMbEgIiIiIqIOY2JBREREREQdxsSCiIiIiIg6jIkFERERERF1GBMLIiJqtZMnT+KPf/wjkpOToVar0atXL9x33304ffp0QP7+lVdeifvvvz8gf4uIiNqGiQUREbXK0aNHMWLECBw+fBhvv/02jhw5gmXLliE/Px/Z2dk4c+ZMl/1tu90u6/0RERETCyIiaqUZM2ZArVbjk08+wejRo9GzZ09cc801+PTTT1FcXIxHHnkEAKBQKPDBBx/4bGsymbBq1Srv94cffhj9+/eHXq9Hnz598Oijj8LhcHiXP/bYYxg2bBhefvll9O7dG1qtFrfddhs+//xzLF68GAqFAgqFAsePHwcA7Nu3D9dccw0MBgMSEhJw6623oqKiwru/K6+8EjNnzsT999+P2NhYjB07tsvOExFRqGJiQURELTpz5gw2bdqEe+65BzqdzmdZYmIiJk+ejDVr1kAI0ar9GY1GrFq1Cvv378fixYuxfPlyPP/88z7rHDlyBO+99x7ef/997N27F4sXL0Z2djamT5+OkpISlJSUIC0tDVVVVbjqqqswfPhwfPvtt9i4cSPKysowceJEn/29+uqrUKvV2LZtG5YtW9axE0JERI0opQ6AiIjk7/DhwxBC4MILL/S7/MILL0RlZSVOnTrVqv397W9/835OT0/H7NmzsXr1ajz00EPe+Xa7Ha+99hri4uK889RqNfR6PRITE73zlixZguHDh2PhwoXeeStWrEBaWhp++ukn9O/fHwDQr18/PPXUU607YCIiajMmFkRE1GotlUio1epW7WfNmjX417/+hYKCApjNZjidTkRGRvqs06tXL5+koinfffcdtmzZAoPB0GhZQUGBN7HIzMxsVWxERNQ+rApFREQt6tu3LxQKBQ4cOOB3+YEDBxAXFweTyQSFQtEoATm3/cT27dsxefJkXHvttfjwww+xZ88ePPLII40aVEdERLQqNrPZjPHjx2Pv3r0+0+HDh3HFFVe0eX9ERNQ+LLEgIqIW9ejRA7m5ufj3v/+NBx54wKedRWlpKd58803MmDEDABAXF4eSkhLv8sOHD8NqtXq/f/XVV+jVq5e3sTcAnDhxolVxqNVquFwun3kXX3wx3nvvPaSnp0Op5M8aEZFUWGJBREStsmTJEtTX12Ps2LH44osvcPLkSWzcuBG5ubno378/5s2bBwC46qqrsGTJEuzZswfffvst7rrrLqhUKu9++vXrh8LCQqxevRoFBQX417/+hXXr1rUqhvT0dOzYsQPHjx9HRUUF3G43ZsyYgTNnzuCWW27BN998g4KCAmzatAnTpk1rlIQQEVHXYWJBRESt0q9fP3zzzTfo06cPJk6ciF69euGaa65B//79sW3bNm8bh2effRZpaWm4/PLL8X//93+YPXs29Hq9dz+//e1v8cADD2DmzJkYNmwYvvrqKzz66KOtimH27NkIDw9HRkYG4uLiUFhYiOTkZGzbtg0ulwtjxozB4MGDcf/998NkMiEsjD9zRESBohCt7RuQiIjoPPPnz8dzzz2HzZs341e/+pXU4RARkYSYWBARUYesXLkS1dXV+POf/8wSAiKiEMbEgoiIiIiIOoyvloiIiIiIqMOYWBARERERUYcxsSAiIiIiog5jYkFERERERB3GxIKIiIiIiDqMiQUREREREXUYEwsiIiIiIuowJhZERERERNRhTCyIiIiIiKjDmFgQEREREVGH/X8jYMQBaVk3cQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "In Table 18.3, we see that if we drop all data after the actual treatment (which occurs between the third and fourth period in the data), and then pretend that the treatment occurred either between the first and second, or second and third periods, we find no DID effect. That’s as it should be! There wasn’t actually a policy change there, so there shouldn’t be a DID effect."
      ],
      "metadata": {
        "id": "fenMSjdPSfrX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(clfe1)\n",
        "print(clfe2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RR0TL-g_S3FE",
        "outputId": "08821d0e-7703-4ca7-cebe-4f1fe951e0ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                          PanelOLS Estimation Summary                           \n",
            "================================================================================\n",
            "Dep. Variable:                   Rate   R-squared:                        0.0019\n",
            "Estimator:                   PanelOLS   R-squared (Between):              0.0004\n",
            "No. Observations:                  81   R-squared (Within):               0.0025\n",
            "Date:                Thu, Nov 02 2023   R-squared (Overall):              0.0004\n",
            "Time:                        03:36:09   Log-likelihood                    240.84\n",
            "Cov. Estimator:             Clustered                                           \n",
            "                                        F-statistic:                      0.0979\n",
            "Entities:                          27   P-value                           0.7556\n",
            "Avg Obs:                       3.0000   Distribution:                    F(1,51)\n",
            "Min Obs:                       3.0000                                           \n",
            "Max Obs:                       3.0000   F-statistic (robust):             0.9733\n",
            "                                        P-value                           0.3285\n",
            "Time periods:                       3   Distribution:                    F(1,51)\n",
            "Avg Obs:                       27.000                                           \n",
            "Min Obs:                       27.000                                           \n",
            "Max Obs:                       27.000                                           \n",
            "                                                                                \n",
            "                             Parameter Estimates                              \n",
            "==============================================================================\n",
            "            Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI\n",
            "------------------------------------------------------------------------------\n",
            "FakeTreat1     0.0061     0.0062     0.9866     0.3285     -0.0063      0.0185\n",
            "==============================================================================\n",
            "\n",
            "F-test for Poolability: 282.21\n",
            "P-value: 0.0000\n",
            "Distribution: F(28,51)\n",
            "\n",
            "Included effects: Entity, Time\n",
            "                          PanelOLS Estimation Summary                           \n",
            "================================================================================\n",
            "Dep. Variable:                   Rate   R-squared:                        0.0019\n",
            "Estimator:                   PanelOLS   R-squared (Between):              0.0004\n",
            "No. Observations:                  81   R-squared (Within):               0.0025\n",
            "Date:                Thu, Nov 02 2023   R-squared (Overall):              0.0004\n",
            "Time:                        03:36:09   Log-likelihood                    240.84\n",
            "Cov. Estimator:             Clustered                                           \n",
            "                                        F-statistic:                      0.0979\n",
            "Entities:                          27   P-value                           0.7556\n",
            "Avg Obs:                       3.0000   Distribution:                    F(1,51)\n",
            "Min Obs:                       3.0000                                           \n",
            "Max Obs:                       3.0000   F-statistic (robust):             0.9733\n",
            "                                        P-value                           0.3285\n",
            "Time periods:                       3   Distribution:                    F(1,51)\n",
            "Avg Obs:                       27.000                                           \n",
            "Min Obs:                       27.000                                           \n",
            "Max Obs:                       27.000                                           \n",
            "                                                                                \n",
            "                             Parameter Estimates                              \n",
            "==============================================================================\n",
            "            Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI\n",
            "------------------------------------------------------------------------------\n",
            "FakeTreat1     0.0061     0.0062     0.9866     0.3285     -0.0063      0.0185\n",
            "==============================================================================\n",
            "\n",
            "F-test for Poolability: 282.21\n",
            "P-value: 0.0000\n",
            "Distribution: F(28,51)\n",
            "\n",
            "Included effects: Entity, Time\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Long-Term Effects\n"
      ],
      "metadata": {
        "id": "VjwphjM6uPDz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib as plt\n",
        "import linearmodels as lm\n",
        "from causaldata import organ_donations\n",
        "od = organ_donations.load_pandas().data\n",
        "\n",
        "# Create Treatment Variable\n",
        "od['California'] = od['State'] == 'California'\n",
        "\n",
        "# Create our interactions by hand,\n",
        "# skipping quarter 3, the last one before treatment\n",
        "for i in [1, 2, 4, 5, 6]:\n",
        "    name = 'INX'+str(i)\n",
        "    od[name] = 1*od['California']\n",
        "    od.loc[od['Quarter_Num'] != i, name] = 0\n",
        "\n",
        "# Set our individual and time (index) for our data\n",
        "od = od.set_index(['State','Quarter_Num'])\n",
        "\n",
        "mod = lm.PanelOLS.from_formula('''Rate ~\n",
        "INX1 + INX2 + INX4 + INX5 + INX6 +\n",
        "EntityEffects + TimeEffects''',od)\n",
        "\n",
        "# Specify clustering when we fit the model\n",
        "clfe = mod.fit(cov_type = 'clustered',\n",
        "cluster_entity = True)\n",
        "\n",
        "# Get coefficients and CIs\n",
        "res = pd.concat([clfe.params, clfe.std_errors], axis = 1)\n",
        "# Scale standard error to CI\n",
        "res['ci'] = res['std_error']*1.96\n",
        "\n",
        "# Add our quarter values\n",
        "res['Quarter_Num'] = [1, 2, 4, 5, 6]\n",
        "# And add our reference period back in\n",
        "reference = pd.DataFrame([[0,0,0,3]],\n",
        "columns = ['parameter',\n",
        "            'lower',\n",
        "            'upper',\n",
        "            'Quarter_Num'])\n",
        "res = pd.concat([res, reference])\n",
        "\n",
        "# For plotting, sort and add labels\n",
        "res = res.sort_values('Quarter_Num')\n",
        "res['Quarter'] = ['Q42010','Q12011',\n",
        "                    'Q22011','Q32011',\n",
        "                    'Q42011','Q12012']\n",
        "\n",
        "# Plot the estimates as connected lines with error bars\n",
        "\n",
        "plt.pyplot.errorbar(x = 'Quarter', y = 'parameter',\n",
        "                    yerr = 'ci', data = res)\n",
        "# Add a horizontal line at 0\n",
        "plt.pyplot.axhline(0, linestyle = 'dashed')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "j9a622DE1hpB",
        "outputId": "a7e0c18c-1397-4efd-ec5b-8e1b8319d58e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.lines.Line2D at 0x7ee2749c7790>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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1FOaMmWKfVlj9LMrOt9+Li4u1kMPPaQJEybUegVjR72fXVVD+3r58uXy8/OTt7e35s+fr1WrVqlt27Y1rktf/8wV99GuyCz76Iceekjh4eHVBgTOxf28n81FnSu1Hjx4UH//+9+1efNmWSyWc27v8OHDGj16tMaNG6c77rijscp0eefq5zP/V1UfeXl5GjNmjPr06aPHH3/8Aiozl4b0c1lZmcaPHy/DMPSPf/yjxva8n2tX376+8sortXXrVh0/flyvv/66xo8frw0bNqhdu3bV2tPXNWMf3TRceR89d+5cLVmyRN9++628vb3rvV6LGeHp3r27LBaLUlJSanw8JSVFISEh+u6773T06FF16tRJ7u7ucnd314EDBzR9+nRFRkZWWycjI0NXXnmlhg0bVm2im1Q5NJiVlVVtWdX9+k6Kbdu2rdzc3GrcTnOdWFvffq7rcMov5efna/To0WrdurU+/PBDeXh42B9rjH52RQ3t56qwc+DAAa1atarG0R1Hv59dVUP7ulWrVurevbuGDh2qN954Q+7u7nrjjTeqrUNfn80V99GuyNX30fPmzdPcuXP15ZdfasCAAQ1at8UEnuDgYP3617/WggULVFRUVO2xzMxMvfPOO5o0aZJuvvlmbd++XVu3brXfwsPD9cADD+iLL76wr3P48GH96le/UkxMjBYtWiSrtXpXxsbGau3atSorK7MvW7VqlXr16qU2bdrUq2ZPT0/FxMRo9erV9mU2m80+k745qm8/11fVmRSenp765JNPzkrzsbGx2rFjR7Wz1qo+0Pv06XNBr6U5a0g/V4WdvXv36quvvlJwcPBZ22uK97OrutD3tM1mU0lJif0+fV0zV9xHuyJX3kc/++yzeuqpp7Ry5UoNGjSoQetKallnae3Zs8do27atcfnllxtr1qwx0tPTjc8//9zo16+fMXDgQCM/P7/G9X45O//QoUNG9+7djZEjRxqHDh0yjhw5Yr9VycnJMUJDQ42bb77Z2Llzp7FkyRLD19fX+Oc//2lvU1JSYmzZssXYsmWL0b59e+P+++83tmzZYuzdu9feZsmSJYaXl5exePFiY9euXcaUKVOMwMDAajPem5v69vOJEyeMLVu2GJ999pkhyViyZImxZcsWez/m5uYaQ4YMMfr372/s27evWj+Xl5cbhlE5U79fv37GqFGjjK1btxorV640QkJCjJkzZ1arqaqfY2JijN/97nfGli1bjOTkZPvj9fldNDf16efS0lLjmmuuMTp27Ghs3bq1Wh9WnSHRlO/n/Px8extJxgsvvGBs2bKlzjPGmoP69PWpU6eMmTNnGomJiUZaWpqxadMm47bbbjO8vLyMnTt3GoZBX5+LK+6jzdzPzWkfPXfuXMPT09P44IMPqj1Pbe+JmrSowGMYlafX3XrrrUZoaKhhsVgMScbYsWONgoKCWtf55R/TokWLDEk13s60bds247LLLjO8vLyMDh06GHPnzj2rlpq2MXz48GrtXn75ZaNTp06Gp6enMXjwYGP9+vUX3A+OVp9+rq0fZ8+ebRiGYXzzzTe19vP+/fvt20lLSzOuuuoqw8fHx2jbtq0xffp0+ymRVWraRufOnavVW5/fRXNzrn6u7XVJMr755hvDMJr2/Vzb7/TWW291ZDc1inP1dVFRkXH99dcb4eHhhqenp9G+fXvjmmuuMTZu3GjfBn19bq62jzZzPzenfXTnzp3rrKU+Wlzg+aVZs2YZfn5+RmJiorNLMTX6uWnQz02Hvm4a9HPTaAn9bDGM8zzZ3kQWLVqk3Nxc3XPPPWcd50XjoZ+bBv3cdOjrpkE/Nw2z9zOBBwAAmJ75IhwAAMAvEHgAAIDpEXgAAIDpEXgAAIDpEXgAAIDpEXgAAIDpEXgAAIDpEXgAAIDpEXgAAIDp/T85peS4U3R20gAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "From Figure 18.6 we can see effects near zero in the three pre-treatment periods - always good, although the confidence interval for the first quarter of 2011 is above zero. That’s not ideal, but as I mentioned, a single dynamic effect behaving badly isn’t a reason to throw out the whole model or anything, especially when the deviation is fairly small in its actual value. We also see three similarly negative effects for the three periods after treatment goes into effect. The impact appears to be immediate and consistent, at least within the time window we’re looking at."
      ],
      "metadata": {
        "id": "PkRhSyJmd60W"
      }
    }
  ]
}