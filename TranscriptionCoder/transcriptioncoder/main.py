import click
import openai
from .audio_processor import AudioProcessor

@click.group()
def cli():
    pass

@click.command()
@click.option('--api_key', prompt='Enter your OpenAI API key', help='Your OpenAI API key')
def setup(api_key):
    openai.api_key = api_key
    click.echo('API key set.')

@click.command()
@click.argument('input_audio')
@click.argument('output_file')
def transcribe(input_audio, output_file):
    click.echo(f'Transcribing {input_audio} to {output_file}...')
    input_audio_file = input_audio
    output_transcript_file = output_file

    audio_processor = AudioProcessor(input_audio_file)
    transcript = audio_processor.transcribe()
    print(transcript)

    with open(output_transcript_file, "w") as f:
        f.write(transcript)



@click.command()
@click.argument('input_transcript')
@click.argument('output_analysis')
def analyze(input_transcript, output_analysis):
    click.echo(f'Analyzing {input_transcript} and saving results to {output_analysis}...')

cli.add_command(setup)
cli.add_command(transcribe)
cli.add_command(analyze)

if __name__ == '__main__':
    cli()
