import boto3
import os


def compare_faces(sourceFile, targetFile):
    client = boto3.client('rekognition')
    message = ""

    imageSource = open('images\\source\\{}'.format(sourceFile), 'rb')
    imageTarget = open('images\\target\\{}'.format(targetFile), 'rb')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        message = ('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()
    return len(response['FaceMatches']), message


def main():
    source_file = 'images\\source\\amanshah.png'
    target_file = 'images\\target\\amanshah.png'
    face_matches = compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))


if __name__ == "__main__":
    main()