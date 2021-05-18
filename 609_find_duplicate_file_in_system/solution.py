class Solution:
    @staticmethod
    def get_filename_and_content(file):
        content_start = file.find("(")
        filename = file[:content_start]
        content = file[content_start+1:-1]
        return filename, content

    @staticmethod
    def name_content_gen(files):
        for file in files:
            yield Solution.get_filename_and_content(file)

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_location_map = collections.defaultdict(list)
        for path in paths:
            temp = path.split(" ")
            location, files = temp[0], temp[1:]
            for filename, content in self.name_content_gen(files):
                content_location_map[content].append(f"{location}/{filename}")
        return list(filter(lambda x: len(x) > 1, content_location_map.values()))
