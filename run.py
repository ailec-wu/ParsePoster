from pa import Pa
from bq import get_quote
import os

pa = Pa(os.environ['pa_user'],os.environ['pa_pass'])
pa.login()
pa.create_post("\n\n".join(get_quote()))

