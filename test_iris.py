#!/usr/bin/env python3
"""Test IRIS agent with a real idea"""

import requests
import json

# Test idea
idea = {
    "title": "Western Union to launch stablecoin",
    "url": "https://www.finextra.com/newsarticle/46830/western-union-to-launch-stablecoin",
    "context": "More than 150 years after introducing its money transfer service, Western Union is launching its own stablecoin.",
    "score": 0.95
}

# Test outline generation
print("=" * 80)
print("Testing Outline Generation")
print("=" * 80)

response = requests.post(
    "http://localhost:8002/v1/outlines",
    json=idea
)

if response.status_code == 200:
    outline = response.json()
    print(f"\n✓ Outline created: {outline['outline_id']}")
    print(f"Hook: {outline['hook']}")
    print(f"\nSections:")
    for section in outline['sections']:
        print(f"\n**{section['heading']}**")
        for point in section['key_points']:
            print(f"  - {point}")
    print(f"\nClosing: {outline['closing']}")

    # Save outline_id for draft test
    outline_id = outline['outline_id']

    # Test draft generation
    print("\n" + "=" * 80)
    print("Testing Draft Generation")
    print("=" * 80)

    draft_request = {
        "outline_id": outline_id,
        "idea": idea,
        "target_length": 800,
        "include_hashtags": True
    }

    response = requests.post(
        "http://localhost:8002/v1/drafts",
        json=draft_request
    )

    if response.status_code == 200:
        draft = response.json()
        print(f"\n✓ Draft created: {draft['draft_id']}")
        print(f"Word count: {draft['word_count']}")
        print(f"Voice score: {draft['voice_score']}")
        print(f"\n{'-'*80}")
        print("DRAFT CONTENT:")
        print(f"{'-'*80}\n")
        print(draft['content'])
        print(f"\n{'-'*80}")
    else:
        print(f"\n✗ Draft generation failed: {response.status_code}")
        print(response.text)
else:
    print(f"\n✗ Outline generation failed: {response.status_code}")
    print(response.text)
