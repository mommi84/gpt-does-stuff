# 💻 gpt-does-stuff
An AI command-line agent based on OpenAI APIs and Docker.

## Setup

- Install requirements:

```bash
pip3 install -r requirements.txt
```

- This project requires [Docker](https://www.docker.com/products/docker-desktop/).
- Add your OpenAI API to the environment variables:

```bash
export OPENAI_API_KEY=<your_key>
```

## Run

```bash
python3 agent.py <model> <instruction>
```

- Model can be `gpt-3.5-turbo` or `gpt-4` (provided you have access to its APIs).

Example:

```bash
python3 agent.py "gpt-3.5-turbo" "print date and time"
```

## Example runs

| Goal                                            | GPT-3.5 | GPT-4 |
|------------------------------------------------:|---------------|-------|
|                             print date and time | ✅ [result](runs/gpt-3.5-turbo_print_date_and_time.md) | ✅ [result](runs/gpt-4_print_date_and_time.md) |
|                   print hello world with Python | ✅ [result](runs/gpt-3.5-turbo_print_hello_world_with_Python.md) | ✅ [result](runs/gpt-4_print_hello_world_with_Python.md) |
|                         perform a Google search | ❌ [result](runs/gpt-3.5-turbo_perform_a_Google_search.md) | ❌ [result](runs/gpt-4_perform_a_Google_search.md) |
| retrieve the value of Europe's total population | ✅ [result](runs/gpt-3.5-turbo_retrieve_the_value_of_Europes_total_population.md) | 🔁 [result](runs/gpt-4_retrieve_the_value_of_Europes_total_population.md) |
|                     implement a tutorial for jq | ❌ [result](runs/gpt-3.5-turbo_implement_a_tutorial_for_jq.md) | ✅ [result](runs/gpt-4_implement_a_tutorial_for_jq.md) |
|                    establish peace in the world | ❌ [result](runs/gpt-3.5-turbo_establish_peace_in_the_world.md) | 🔁 [result](runs/gpt-4_establish_peace_in_the_world.md) |

✅ goal achieved
❌ goal missed
🔁 endless loop
