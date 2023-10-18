from django.core.exceptions import ValidationError

from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StreamBlockValidationError,
    StructBlock,
    StructValue,
    TextBlock,
    URLBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    alt_text = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """

    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a header size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribute_name = CharBlock(blank=True, required=False, label="e.g. Mary Berry")

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"


class LinkStructValue(StructValue):
    def url(self):
        external_url = self.get("external_url")
        page = self.get("page")
        return external_url or page.url


class LinkBlock(StructBlock):
    text = CharBlock()
    page = PageChooserBlock(required=False)
    external_url = URLBlock(required=False, label="External URL")
    aria_label = CharBlock(required=False, label="ARIA label")

    class Meta:
        value_class = LinkStructValue
        template = "blocks/link_block.html"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="pilcrow", template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
        template="blocks/embed_block.html",
    )
    link_block = LinkBlock()

    def clean(self, value):
        result = super().clean(value)

        headings = [
            # tuples of block index and heading level
            (0, 1)  # mock H1 block at index 0
        ]
        errors = {}

        # first iterate through all blocks in the StreamBlock
        for i in range(1, len(result)):  # result indexes begin at 1
            # if a block is of type "heading_block?
            if result[i].block_type == "heading_block":
                # convert size string to integer
                level = int(result[i].value.get("size")[-1:])
                # append tuple of block index and heading level to list
                headings.append((i, level))

        # now iterate through list of headings,
        # starting with second heading to skip over the mock H1 heading block
        for i in range(1, len(headings)):
            # compare its level to the previous heading's level
            if int(headings[i][1]) - int(headings[i-1][1]) > 1:
                # if the difference is more than 1,
                # add an error to the array with its original index
                errors[headings[i][0]] = ValidationError(
                    "Incorrect heading hierarchy. Avoid skipping levels."
                )

        if errors:
            raise StreamBlockValidationError(block_errors=errors)

        return result
