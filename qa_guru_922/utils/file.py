def abs_path_frog_project(relative_path: str):
    import qa_guru_922
    from pathlib import Path

    return (
        Path(qa_guru_922.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
