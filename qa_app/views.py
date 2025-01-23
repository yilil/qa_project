from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Question
from langchain.prompts import PromptTemplate
import os
from resource_manager import resource_manager
from qa_project.settings import api_name


def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})


def ask_question(request):
    if api_name not in os.environ:
        messages.error(request, f"You need to save your {api_name} key as an environment variable!")
        return redirect('home')

    if request.method == 'POST':
        question = request.POST.get('question')

        llm = resource_manager.get_llm()
        retriever = resource_manager.get_vector_store().as_retriever(search_kwargs={"k": 2})

        try:
            prompt_template = PromptTemplate(
                input_variables=["context", "question"],
                template="""Given the context below, answer the question. If the provided context is irrelevant to the question, answer with your background knowledge.
                
                Context:
                {context}
                
                Question:
                {question}
                
                Answer:"""
            )

            # Retrieve the relevant context
            documents = retriever.invoke(question)
            context = "\n".join([doc.page_content for doc in documents])

            print(f"Context: {context}")

            chain = prompt_template | llm
            answer = chain.invoke({"question": question, "context": context}).content

            # Save to database
            Question.objects.create(
                question_text=question,
                answer=answer
            )

            messages.success(request, 'Question answered successfully!')
        except Exception as e:
            messages.error(request, f'Error processing question: {str(e)}')

    return redirect('home')
