from openai import OpenAI
client = OpenAI()

batch_job = client.batches.cancel('batch_EadWwL2GIZOmNzxR3r2bQ0Bw')
print(batch_job)
