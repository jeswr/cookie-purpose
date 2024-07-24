from openai import OpenAI
client = OpenAI()

batch_file = client.files.create(
  file=open("batch_purposes_0.jsonl", "rb"),
  purpose="batch"
)

batch_job = client.batches.create(
  input_file_id=batch_file.id,
  endpoint="/v1/chat/completions",
  completion_window="24h"
)

print(batch_job, batch_file.id)
# Batch(id='batch_EadWwL2GIZOmNzxR3r2bQ0Bw', completion_window='24h', created_at=1721827602, endpoint='/v1/chat/completions', input_file_id='file-XsMwQQR8O43AAJzcfG8QThtS', object='batch', status='validating', cancelled_at=None, cancelling_at=None, completed_at=None, error_file_id=None, errors=None, expired_at=None, expires_at=1721914002, failed_at=None, finalizing_at=None, in_progress_at=None, metadata=None, output_file_id=None, request_counts=BatchRequestCounts(completed=0, failed=0, total=0)) file-XsMwQQR8O43AAJzcfG8QThtS