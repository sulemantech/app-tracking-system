# candidate_matching/tfidf_matcher.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_job(resume_text, job_description):
    """Match a resume to a job description using TF-IDF."""
    
    # Combine resume and job description into a list
    documents = [resume_text, job_description['description']]
    
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Compute the cosine similarity between the resume and job description
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    # Return the similarity score
    return cosine_sim[0][0]
