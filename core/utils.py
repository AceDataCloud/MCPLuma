"""Utility functions for MCP Luma server."""

from typing import Any


def format_video_result(data: dict[str, Any]) -> str:
    """Format video generation result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if not data.get("success", False):
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    lines = [
        f"Task ID: {data.get('task_id', 'N/A')}",
        f"Video ID: {data.get('video_id', 'N/A')}",
        f"State: {data.get('state', 'N/A')}",
        "",
        f"Prompt: {data.get('prompt', 'N/A')}",
        "",
        "Video Info:",
        f"  URL: {data.get('video_url', 'N/A')}",
        f"  Width: {data.get('video_width', 'N/A')}",
        f"  Height: {data.get('video_height', 'N/A')}",
        "",
        "Thumbnail Info:",
        f"  URL: {data.get('thumbnail_url', 'N/A')}",
        f"  Width: {data.get('thumbnail_width', 'N/A')}",
        f"  Height: {data.get('thumbnail_height', 'N/A')}",
        "",
    ]

    return "\n".join(lines)


def format_task_result(data: dict[str, Any]) -> str:
    """Format task query result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if "error" in data:
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    request_info = data.get("request", {})
    response_info = data.get("response", {})

    lines = [
        f"Task ID: {data.get('id', 'N/A')}",
        f"Created At: {data.get('created_at', 'N/A')}",
        "",
        "Request:",
        f"  Action: {request_info.get('action', 'N/A')}",
        f"  Prompt: {request_info.get('prompt', 'N/A')}",
        "",
    ]

    if response_info.get("success"):
        lines.append("Response: Success")
        lines.append("")
        lines.extend(
            [
                f"Video ID: {response_info.get('video_id', 'N/A')}",
                f"Video URL: {response_info.get('video_url', 'N/A')}",
                f"Video Size: {response_info.get('video_width', 'N/A')}x{response_info.get('video_height', 'N/A')}",
                f"State: {response_info.get('state', 'N/A')}",
                "",
                f"Thumbnail URL: {response_info.get('thumbnail_url', 'N/A')}",
            ]
        )
    else:
        lines.append(f"Response: {response_info}")

    return "\n".join(lines)


def format_batch_task_result(data: dict[str, Any]) -> str:
    """Format batch task query result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if "error" in data:
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    lines = [f"Total Tasks: {data.get('count', 0)}", ""]

    for item in data.get("items", []):
        response_info = item.get("response", {})
        lines.extend(
            [
                f"=== Task: {item.get('id', 'N/A')} ===",
                f"Created At: {item.get('created_at', 'N/A')}",
                f"Success: {response_info.get('success', False)}",
                f"Video URL: {response_info.get('video_url', 'N/A')}",
                "",
            ]
        )

    return "\n".join(lines)
