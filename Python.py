{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOexq6So6/pVgqsf8O+WxJ0"
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
      "source": [
        "In Python Everything is an object"
      ],
      "metadata": {
        "id": "JLMKLTVGYh8m"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Hello World\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "Gy96joO7gtdf",
        "outputId": "1eb59d63-7d3a-4027-81f8-f8267207b59d"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(5)"
      ],
      "metadata": {
        "collapsed": true,
        "id": "iHDhVZong0Ze",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d2f5ce87-4e18-4de6-d556-d36594aed7e3"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(17*14)"
      ],
      "metadata": {
        "collapsed": true,
        "id": "0PVTnVK0h6uM",
        "outputId": "925b8eaa-4260-490f-9bb2-9f73b95f9bd2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "238\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"single - line comment\") # singleline comment"
      ],
      "metadata": {
        "id": "-v8bIu-_kH8S",
        "collapsed": true,
        "outputId": "802eaaa9-88b9-408f-c5e3-3c2a80f21c79",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "single - line comment\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Hello\" , 6 , 7, sep = \" \"  , end = \"001\")  # same line  print + seprator\n",
        "print(\" \\\"Good morning\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LwFGlUMj90y3",
        "outputId": "8b39b553-ece5-40ca-c5ab-03d29c27f4e7",
        "collapsed": true
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello 6 7001 \"Good morning\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"hello I am good boy \\n and also a good person\")  # new line"
      ],
      "metadata": {
        "collapsed": true,
        "id": "stQmiX0SjRxq",
        "outputId": "9803d8b9-e677-4f01-bc48-f8d1ce38bc09",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello I am good boy \n",
            " and also a good person\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"hello \\\"I am good boy\\\"  and also a good person\") #escape sequence"
      ],
      "metadata": {
        "id": "wlWMQAIKxXQA",
        "collapsed": true,
        "outputId": "372a9920-acf3-40ec-b7c3-8d21e816cb08",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello \"I am good boy\"  and also a good person\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 12            # we cannot add a number with the string  +  data type check\n",
        "b = 10\n",
        "c = a + b\n",
        "print(c)\n",
        "print(\"The type of this variable is\" , type(c))"
      ],
      "metadata": {
        "collapsed": true,
        "id": "sAunXn5zNWdK",
        "outputId": "ed914f68-ec3c-415a-bbad-190aeae26e21",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "22\n",
            "The type of this variable is <class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = complex(8, 2) # complex number\n",
        "print(a)\n",
        "print(type(a))"
      ],
      "metadata": {
        "collapsed": true,
        "id": "3bgvmIDJPRTB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8dbedb30-48b3-40c3-8eda-7b3a2c5f3e4e"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(8+2j)\n",
            "<class 'complex'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"Tushar\"\n",
        "age = 31\n",
        "price = 25.11\n",
        "\n",
        "print(type(name));\n",
        "print(name);\n",
        "print(type(age));\n",
        "print(age);\n",
        "print(type(price));\n",
        "print(price);"
      ],
      "metadata": {
        "id": "P8pDr1gCJ2k5",
        "collapsed": true,
        "outputId": "1ecff9f9-9ba7-4e70-fe20-7ae575446a3a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n",
            "Tushar\n",
            "<class 'int'>\n",
            "31\n",
            "<class 'float'>\n",
            "25.11\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 1000\n",
        "b = 500\n",
        "sum = a + b\n",
        "print(type(sum))\n",
        "print(sum)"
      ],
      "metadata": {
        "id": "S3O0JZIvijmL",
        "collapsed": true,
        "outputId": "eeaa3dd9-2738-4509-d8f7-04abafba186f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n",
            "1500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 1000\n",
        "b = 500\n",
        "diff = a - b\n",
        "print(type(diff))\n",
        "print(diff)"
      ],
      "metadata": {
        "collapsed": true,
        "id": "0L3Qmwk3cFXr",
        "outputId": "5c097742-f768-40f0-fbe9-c78dd8f329e3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n",
            "500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a =  eval (input(\"Enter a no.\"))\n",
        "print(a*2)\n",
        "type(a)"
      ],
      "metadata": {
        "id": "ggp8N9Tjkq0x",
        "collapsed": true,
        "outputId": "097f05d1-b7cc-4222-ca83-d083d8748dcc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a no.2\n",
            "4\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"The teacher asked, \\\" Show me your homework.\\\" \")"
      ],
      "metadata": {
        "id": "gwyPh3H_Ce6m",
        "collapsed": true,
        "outputId": "135062c1-5b57-4e5b-c1fd-6517d0b582b2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The teacher asked, \" Show me your homework.\" \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"Tushar\"\n",
        "middleName = 'Kant'\n",
        "lastName = \"Behera\"\n",
        "\n",
        "print  (\"Hello\" , name , middleName , lastName)                  #strings"
      ],
      "metadata": {
        "id": "dho7yaobCytc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1fe0d2a7-96f8-443a-a04b-872cc56909b7",
        "collapsed": true
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello Tushar Kant Behera\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "eat = 'I want to eat an , \"Apple\"'\n",
        "                                                                    # Single cottes '' inside double \"\"\n",
        "print(eat)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "StjO37j6rgsC",
        "outputId": "03651b03-9a94-431f-93f1-95992e43431e"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "I want to eat an , \"Apple\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "hello = '''i\n",
        "am\n",
        "tushar'''                                                                 # use triple cottes''' print multiple lines\n",
        "print(hello)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "sxCFQMuzsMHp",
        "outputId": "280d0577-6381-4590-e238-b0505adcb7bd"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "i \n",
            "am\n",
            "tushar\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for letter in \"help you online is great\":\n",
        "    if letter == 'e' or letter == 's':\n",
        "        break\n",
        "    print(\"current letter:\", letter)"
      ],
      "metadata": {
        "id": "tsUu7MiPBQ6f",
        "collapsed": true,
        "outputId": "715e4492-011d-4d43-c3e9-6255511c1f9f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "current letter: h\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for letter in \"help you online is great\":\n",
        "    if letter == 'e' or letter == 's':\n",
        "        continue\n",
        "    print(\"current letter:\", letter)"
      ],
      "metadata": {
        "collapsed": true,
        "id": "bL6Hz7a5j57Q",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c90ccff0-4b7e-4098-8182-905b2b1e3912"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "current letter: h\n",
            "current letter: l\n",
            "current letter: p\n",
            "current letter:  \n",
            "current letter: y\n",
            "current letter: o\n",
            "current letter: u\n",
            "current letter:  \n",
            "current letter: o\n",
            "current letter: n\n",
            "current letter: l\n",
            "current letter: i\n",
            "current letter: n\n",
            "current letter:  \n",
            "current letter: i\n",
            "current letter:  \n",
            "current letter: g\n",
            "current letter: r\n",
            "current letter: a\n",
            "current letter: t\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def display_number(number):\n",
        "    if number == 2:\n",
        "        pass\n",
        "    else:\n",
        "        print(number)\n",
        "\n",
        "display_number(2)\n",
        "display_number(3)"
      ],
      "metadata": {
        "collapsed": true,
        "id": "3pB_ayONntkW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "88198b4c-2695-4bc7-f6f6-541c30d99a04"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lists = [ 8 , 2 , 3  , [ 5.5 , 2.3 ]  , [\"apple\" , \"mango\"]] #mutable\n",
        "print(lists)\n",
        "print(type(lists))"
      ],
      "metadata": {
        "id": "qERJYCQnVX_T",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "outputId": "6adbdb2d-6d3b-4fab-fe28-6b98ecc95578"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[8, 2, 3, [5.5, 2.3], ['apple', 'mango']]\n",
            "<class 'list'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tuples = ( 8 , 2 , 3  , ( 5.5 , 2.3 )  , [\"apple\" , \"mango\"]);\n",
        "print(tuples);\n",
        "print(type(tuples));\n",
        "                                                                                                    # immutble"
      ],
      "metadata": {
        "id": "vnt-JaWDWoy4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "outputId": "8c93002d-4abb-4f13-d8d7-3db5123d31b1"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(8, 2, 3, (5.5, 2.3), ['apple', 'mango'])\n",
            "<class 'tuple'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dicts = { \"name\":\"Sakshi\" , \"age\":32 , \"city\":\"Pune\"}\n",
        "print(dicts)\n",
        "print(type(dicts))"
      ],
      "metadata": {
        "id": "Cez2FIL0XJI_",
        "collapsed": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "acf993cf-edee-46b8-a59d-91ccd23bfcac"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'name': 'Sakshi', 'age': 32, 'city': 'Pune'}\n",
            "<class 'dict'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a  = eval(input(\"Enter a number for Addition = \"))\n",
        "b  = eval(input(\"Enter b number for Addition = \"))          #Addition\n",
        "print(a + b)\n",
        "print(type(a))\n",
        "print(type(b))\n",
        "\n",
        "a1 = eval(input(\"Enter a number for subtraction = \"))          #Subtraction\n",
        "b1 = eval(input(\"Enter b number for subtraction = \"))\n",
        "print(a1 - b1)\n",
        "print(type(a1))\n",
        "print(type(b1))\n",
        "\n",
        "\n",
        "a2  = eval(input(\"Enter a number for Division = \"))         #Divison\n",
        "b2  = eval(input(\"Enter b number for Division = \"))\n",
        "print(a2 / b2)\n",
        "print(type(a))\n",
        "print(type(b))\n",
        "\n",
        "a3  = eval(input(\"Enter a number for Multiplication = \"))       #Multiplication\n",
        "b3  = eval(input(\"Enter b number for Multiplication = \"))\n",
        "print(a3 * b3)\n",
        "print(type(a3))\n",
        "print(type(b3))\n",
        "\n",
        "a4  = eval(input(\"Enter a number for Exponent = \"))         #Exponent\n",
        "b4  = eval(input(\"Enter b number for Exponent = \"))\n",
        "print(a4 ** b4)\n",
        "print(type(a4))\n",
        "print(type(b4))\n",
        "\n",
        "a5  = eval(input(\"Enter a number for floor division = \"))       #floor division\n",
        "b5  = eval(input(\"Enter b number for floor division = \"))\n",
        "print(a5 // b5)\n",
        "print(type(a5))\n",
        "print(type(b5))\n",
        "\n",
        "a6  = eval(input(\"Enter a number for modulous = \"))         # Modulous\n",
        "b6  = eval(input(\"Enter b number for modulous = \"))\n",
        "print(a6 % b6)\n",
        "print(type(a6))\n",
        "print(type(b6))\n"
      ],
      "metadata": {
        "collapsed": true,
        "id": "Ck2a-37qyD3N",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fdc57892-f022-472f-ab04-b09ca2f90b9c"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number for Addition = 2\n",
            "Enter b number for Addition = 2\n",
            "4\n",
            "<class 'int'>\n",
            "<class 'int'>\n",
            "Enter a number for subtraction = 3\n",
            "Enter b number for subtraction = 3\n",
            "0\n",
            "<class 'int'>\n",
            "<class 'int'>\n",
            "Enter a number for Division = 4\n",
            "Enter b number for Division = 6\n",
            "0.6666666666666666\n",
            "<class 'int'>\n",
            "<class 'int'>\n",
            "Enter a number for Multiplication = 5\n",
            "Enter b number for Multiplication = 5\n",
            "25\n",
            "<class 'int'>\n",
            "<class 'int'>\n",
            "Enter a number for Exponent = 4\n",
            "Enter b number for Exponent = 2\n",
            "16\n",
            "<class 'int'>\n",
            "<class 'int'>\n",
            "Enter a number for floor division = 4\n",
            "Enter b number for floor division = 4\n",
            "1\n",
            "<class 'int'>\n",
            "<class 'int'>\n",
            "Enter a number for modulous = 2\n",
            "Enter b number for modulous = 4\n",
            "2\n",
            "<class 'int'>\n",
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = \"1\"                           #Basic TypeCasting\n",
        "b = \"2\"\n",
        "print(int(a) + int(b))"
      ],
      "metadata": {
        "id": "nM1XoFdy8Z6n",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "outputId": "d91ab5c6-f340-475e-e857-ac7231b04d0b"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "string = \"15\"\n",
        "number = 7\n",
        "string_number = int(string)  # throws an error if the string is not a valid integer Explicit TypeCasting\n",
        "\n",
        "sum = number + string_number\n",
        "print(\"The sum of both the numbers is: \", sum)"
      ],
      "metadata": {
        "id": "dwBy94NC9rwL",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "outputId": "ec1e611a-078f-4cd2-f259-32adbee6aaaa"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The sum of both the numbers is:  22\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Python automatically converts\n",
        "# a to int\n",
        "a = 7\n",
        "print(type(a))\n",
        "                                                                                              #Implicit TypeCasting\n",
        "# Python automatically converts b\n",
        "# to float\n",
        "b = 3.0\n",
        "print(type(b))\n",
        "\n",
        "# Python automatically converts c\n",
        "# to float as it is a float addition\n",
        "c = a + b\n",
        "print(c)\n",
        "print(type(c))"
      ],
      "metadata": {
        "id": "67VeunsP-2f9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "outputId": "0a99c46e-0887-47d8-fef6-d41536c908b8"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n",
            "<class 'float'>\n",
            "10.0\n",
            "<class 'float'>\n"
          ]
        }
      ]
    }
  ]
}
