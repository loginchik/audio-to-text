import os.path
import sys
import datetime
import logging

import whisper as wh

AUDIO_FORMATS = ["mp3", "m4a", "webm", "mp4", "mpga", "wav", "mpeg"]
MODEL_LEVELS = ["tiny", "base", "small", "medium", "large"]


def configure_paths(source_path, output_path):
    source_path = os.path.abspath(source_path)
    output_path = os.path.abspath(output_path)
    output_file = f'{datetime.datetime.now().strftime("%Y%m%d_%H%M%S_text")}.txt'
    output_path = os.path.join(output_path, output_file)
    return source_path, output_path


def check_source(source_path: str) -> str | None:
    if not os.path.exists(source_path):
        return "Check source path"
    elif not source_path.split('.')[-1] in AUDIO_FORMATS:
        return "Source file type not supported"
    else:
        return None


def check_output_path(output_path: str) -> str | None:
    if not (os.path.exists(output_path) and os.path.isdir(output_path)):
        return "Output folder must exist and be a directory"


def configure_model():
    model_level = input('Enter model level (any from: {}, default is "base", press Enter to default):'.format(', '.join(MODEL_LEVELS)))
    if not model_level in MODEL_LEVELS:
        model_level = "base"

    logging.info("Loading model")
    model = wh.load_model(model_level, download_root="models/")
    logging.info("Model loaded")
    return model


def get_source_path() -> str | None:
    source_path = input('Enter source file (formats: {}):'.format('|'.join(AUDIO_FORMATS)))
    source_check = check_source(source_path)
    if not source_check is None:
        logging.fatal(source_check)
        sys.exit(2)
    else:
        source_path = os.path.abspath(source_path)
        return source_path


def get_output_path(source_path: str) -> str | None:
    output_path = input('Enter output directory (Downloads by default, press Enter to skip):')
    if output_path == '':
        output_path = os.path.expanduser('~/Downloads')
    output_check = check_output_path(output_path)
    if not output_check is None:
        logging.fatal(output_check)
        sys.exit(2)
    else:
        output_path = os.path.abspath(output_path)
        original_name = source_path.split("/")[-1].split(".")[0]
        datestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f'{original_name}_{datestamp}_text.txt'
        output_path = os.path.join(output_path, output_file)

        logging.info("Output file is set to {}".format(output_path))
        return output_path


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt="%Y-%m-%d %H:%M:%S")
    source_path = get_source_path()

    logging.info("Loading audio from {}".format(source_path))
    audio = wh.load_audio(source_path)
    logging.info("Audio loaded")

    output_path = get_output_path(source_path)

    model = configure_model()

    logging.info("Transcribing text. It may take a while...")
    result = model.transcribe(audio=audio, fp16=False)
    logging.info("Finished")

    logging.info("Saving result")
    with open(output_path, 'w') as f:
        f.write(result['text'])
    logging.info("Text saved to {}".format(output_path))
    sys.exit()
