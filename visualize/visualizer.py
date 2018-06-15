import os
import pytagcloud

RESULT_DIRECTORY = "__results__/visualization"


def wordcloud(filename, wordfreq):
    taglist = pytagcloud.make_tags(wordfreq.items(), maxsize=80)
    # print(taglist)
    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(
        taglist,
        save_filename,
        size=(900, 600),
        fontname='Malgun',
        rectangular=False,
        background=(0, 0, 0))


if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)