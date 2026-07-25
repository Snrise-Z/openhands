from litellm import ChatCompletionToolParam, ChatCompletionToolParamFunctionChunk

from openhands.llm.tool_names import EXPAND_TOOL_NAME


ExpandTool = ChatCompletionToolParam(
    type='function',
    function=ChatCompletionToolParamFunctionChunk(
        name=EXPAND_TOOL_NAME,
        description=(
            'Return the exact original text of a previous compressed observation. '
            'Use this before copying exact code, identifiers, or old_str values from '
            'a compressed tool result. Previous tool results include an Observation ID '
            'such as obs_000042; pass that id as source_observation_id.'
        ),
        parameters={
            'type': 'object',
            'properties': {
                'source_observation_id': {
                    'description': 'The Observation ID shown in a previous tool result, e.g. obs_000042.',
                    'type': 'string',
                },
            },
            'required': ['source_observation_id'],
        },
    ),
)
