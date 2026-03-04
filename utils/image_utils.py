from caption import generate_caption
from vqa import answer_question

def process_image(image, question):

    caption = generate_caption(image)

    answer = answer_question(image, question)

    return caption, answer