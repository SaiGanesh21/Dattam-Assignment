import pandas as pd
import fasttext
from fasttext import load_model
from pycountry import languages

def detect_language(text, model):
 
    if isinstance(text, str):
      
        predictions = model.predict(text)
        language_code = predictions[0][0].split('__')[-1]
     
        lang = languages.get(alpha_2=language_code)
        if lang==None:
            language='Unknown language'
        else:
            language=lang.name
        return language
        
    return 'Not a string'

def main(input_file, output_file, model_file):
    # Load the parquet file
    df = pd.read_parquet(input_file)  
         
    # Load the FastText model
    model = fasttext.load_model(model_file)
    
    # Remove new lines from position
    df['position'] = df['position'].str.replace('\n', ' ')
    # Detect language
    df['language'] = df['position'].apply(lambda text: detect_language(text, model))
    
    # Save the updated DataFrame to the output file
    df.to_parquet(output_file)
    df_output = pd.read_parquet('output.parquet')
    print(df_output)
    

if __name__ == '__main__':
    input_file = 'input.parquet'
    output_file = 'output.parquet'
    model_file = 'lid.176.bin'

    main(input_file, output_file, model_file)